
from simple_pid import PID  # type:ignore

from vessel_common import parameter_store, savable, time

from lib.controllers import controller




class AdditionController(controller.Controller, controller.AssignableController):
    def __init__(
        self,
        ps: parameter_store.ParameterStore,
        pump_name: str,
        assignment: typing.Dict[str, typing.Any],
        config: controller.ConfigType,
        additional_ps_keys: typing.Dict[str, typing.Any] = None,
        no_ps_set_keys: typing.List[str] = None,
        **kwargs: typing.Any,
    ):
        controller.Controller.__init__(
            self, config, "addition_controller", ps=ps, **kwargs
        )
        controller.AssignableController.__init__(self, assignment)
        self.all_keys = self.optional_keys()
        self.all_keys.update(self.assignment)
        self.all_keys.update(additional_ps_keys or {})
        self.pump_name = pump_name
        self.set_keys_in_ps(no_ps_set_keys)

        self.rate_setpoint_topic = "{}_rate_setpoint".format(self.pump_name)

    def assign_scale_feedback_pump_controller(self):
        """Tells the pump controller to use scale feedback to follow the setpoint we will
        publish."""
        self.ps.priority_set(
            "controller/pump/assignment/{}".format(self.pump_name),
            {
                "pump_controller_class_name": "ScaleFeedbackPumpController",
                "pump_name": self.pump_name,
                "feedback_scale_name": self.assignment["feedback_scale_name"],
                "density": self.assignment["density"],
                "evaporation_rate_gph": self.assignment["evaporation_rate_gph"],
            },
        )

    def assign_open_loop_pump_controller(self):
        """Tells the pump controller to follow the setpoint without scale feedback."""
        self.ps.priority_set(
            "controller/pump/assignment/{}".format(self.pump_name),
            {
                "pump_controller_class_name": "OpenLoopPumpController",
                "pump_name": self.pump_name,
            },
        )

    def set_keys_in_ps(self, no_ps_set_keys):
        for k, v in self.all_keys.items():
            if no_ps_set_keys and k in no_ps_set_keys:
                continue
            setattr(self, k, v)  # default values
            self.ps.set("controller/addition/{0}/{1}".format(self.pump_name, k), v)

    def update(self, dt: float) -> None:
        state = box.Box()
        for k in self.all_keys:
            state[k] = self.ps.get(
                "controller/addition/{0}/{1}".format(self.pump_name, k),
                should_raise=False,
            )
            # Revert to default if not found in PS.
            if state[k] is None:
                state[k] = getattr(self, k)
        self.update_add_control(state)

    @abc.abstractmethod
    def update_add_control(self, state):
        raise NotImplementedError()

    @classmethod
    def required_keys(cls):
        return []


class ScaleFeedbackAdditionController(AdditionController):
    @classmethod
    def required_keys(cls):
        return super().required_keys() + [
            "feedback_scale_name",
            "density",
            "evaporation_rate_gph",
        ]

class TimedAdditionControllerMixin(savable.Savable):
    def __init__(self):
        super(TimedAdditionControllerMixin, self).__init__(register=False)
        self.duration_timer = time.TimeHelper(
            period=self.duration, ready_immediately=False
        )
        # Since the duration time will restart we will mark the first time we are
        # finished with it so we don't repeat
        self.finished = False

    def attributes_to_save(self):
        return savable.Savable.attributes_to_save(self) + ["finished", "duration_timer"]

class TimedScaleFeedbackAdditionController(
    ScaleFeedbackAdditionController, TimedAdditionControllerMixin
):
    def __init__(self, *args, **kwargs):
        ScaleFeedbackAdditionController.__init__(self, *args, **kwargs)
        TimedAdditionControllerMixin.__init__(self)

    def attributes_to_save(self):
        return ScaleFeedbackAdditionController.attributes_to_save(
            self
        ) + TimedAdditionControllerMixin.attributes_to_save(self)

class LinearAdditionController(TimedScaleFeedbackAdditionController):
    """Commands a rate that increases or decreases at a linear rate."""

    def __init__(
        self,
        ps: parameter_store.ParameterStore,
        pump_name: str,
        assignment: typing.Dict[str, typing.Any],
        config: controller.ConfigType,
        additional_ps_keys: typing.Optional[typing.Dict[str, typing.Any]] = None,
        **kwargs: typing.Any,
    ):
        if not additional_ps_keys:
            additional_ps_keys = {}

        if "slope" not in additional_ps_keys:
            # Calculate the linear params.
            if assignment["duration"] == 0:
                slope = 0.0
            else:
                slope = (
                    float(assignment["end_rate"] - assignment["start_rate"])
                    / assignment["duration"]
                )
            additional_ps_keys["slope"] = slope
            additional_ps_keys["intercept"] = assignment["start_rate"]

        super().__init__(
            ps,
            pump_name,
            assignment,
            config,
            additional_ps_keys=additional_ps_keys,
            **kwargs,
        )

        self.assign_scale_feedback_pump_controller()

        self.previous_process_volume = 0.0
        self.initial_volume: Optional[float] = None
        self.multiplier = 1.0

    def attributes_to_save(self):
        return super().attributes_to_save() + ["previous_process_volume"]

    @classmethod
    def required_keys(cls):
        return super().required_keys() + ["duration", "end_rate", "start_rate"]

    @classmethod
    def optional_keys(cls):
        return {
            **super().optional_keys(),
            "feed_relative_to_process_volume": False,
            "feed_relative_to_process_volume_threshold": 0.75,
            "continuous_volume_adjustment": False,
            "correction_factor": None,
            "on_off_cycle_num": None,
            "on_off_cycle_inverse": False,
        }

    def get_new_setpoint(self, state):
        self.duration_timer.set_period(state.duration)
        seconds = self.duration_timer.elapsed_since_ready()
        rate = state.slope * seconds + state.intercept
        if state.correction_factor is not None:
            rate *= state.correction_factor
        return rate

    def update_add_control(self, state):
        if self.finished:
            self.logger.info("LinearAdditionController already finished with duration.")
            return

        if self.duration_timer.ready():
            self.logger.info("LinearAdditionController shutting down: Duration elapsed")
            self.shutdown()
            return
        # Calculate a new pumping rate.
        new_setpoint = self.get_new_setpoint(state)

        # First get the initial volume at the start of feeding
        if self.initial_volume is None:
            try:
                self.initial_volume = self.ps.get("process_volume/total")
            except KeyError:
                self.logger.error("LinearAdditionController: no process volume.")
        # Get the current total volume
        total_volume = self.ps.get("process_volume/total", should_raise=False)
        # Adjust the rate if the current process volume is less than the previous volume
        # by more than the threshold
        if state.feed_relative_to_process_volume:
            if total_volume:
                if self.previous_process_volume != 0 and (
                    total_volume
                    < self.previous_process_volume
                    - state.feed_relative_to_process_volume_threshold
                ):
                    self.multiplier *= total_volume / self.previous_process_volume
                new_setpoint *= self.multiplier
                self.previous_process_volume = total_volume
            else:
                self.logger.error("LinearAdditionController: no process volume.")
        # Check if we should do continuous volume adjustment
        if state.continuous_volume_adjustment and self.initial_volume:
            # Adjust the rate setpoint by the volume compared to
            # initial volume when controller was initialized
            if total_volume:
                ratio = total_volume / self.initial_volume
                new_setpoint *= ratio
            else:
                self.logger.error("LinearAdditionController: no process volume.")

        if state.on_off_cycle_num is not None:
            modulator_en = self.ps.get(
                f"on_off_enable_{state.on_off_cycle_num}", should_raise=False
            )
            if modulator_en:
                mod_signal = self.ps.get(
                    f"on_off_cycle_{state.on_off_cycle_num}", should_raise=False
                )
                if (mod_signal == 0 and not state.on_off_cycle_inverse) or (
                    mod_signal == 1 and state.on_off_cycle_inverse
                ):
                    new_setpoint = 0

        self.logger.debug(
            "LinearAdditionController: now pumping at {} rate.".format(new_setpoint)
        )
        self.ps.priority_set("{}_rate_setpoint".format(self.pump_name), new_setpoint)

    def shutdown(self):
        self.finished = True
        self.ps.priority_set("{}_rate_setpoint".format(self.pump_name), 0)
        # Release the pump assignment
        self.ps.priority_set(
            "controller/pump/assignment/{}".format(self.pump_name), None
        )


class SteppedLinearAdditionController(LinearAdditionController):
    """Commands a rate that increases or decreases at a linear rate."""

    def __init__(
        self,
        ps: parameter_store.ParameterStore,
        pump_name: str,
        assignment: typing.Dict[str, typing.Any],
        config: controller.ConfigType,
        **kwargs: typing.Any,
    ):
        # Put the slope in for the first profile
        slope, intercept, duration = self.calc_profile(assignment["schedule"][0])
        additional_ps_keys = {
            "slope": slope,
            "intercept": intercept,
            "duration": duration,
            "profile_i": 0,
        }

        super().__init__(
            ps,
            pump_name,
            assignment,
            config,
            additional_ps_keys=additional_ps_keys,
            **kwargs,
        )

    def calc_profile(self, profile):
        slope = float(profile["end_rate"] - profile["start_rate"]) / profile["duration"]
        return slope, profile["start_rate"], profile["duration"]

    @classmethod
    def required_keys(cls):
        # Skip over parent, we control the start and end rates
        return TimedScaleFeedbackAdditionController.required_keys() + [
            "schedule",
        ]

    def update_add_control(self, state):
        if self.finished:
            self.logger.info(
                "SteppedLinearAdditionController already finished with duration."
            )
            return

        if self.duration_timer.ready():
            # Move on to next profile
            profile_i = state.profile_i
            profile_i += 1
            if profile_i >= len(state.schedule):
                self.logger.info(
                    "SteppedLinearAdditionController: done with schedule, shutting down"
                )
                self.shutdown()
                return

            slope, intercept, duration = self.calc_profile(state.schedule[profile_i])
            self.logger.info(
                f"SteppedLinearAdditionController: moving to profile {profile_i} with slope {slope}, intercept {intercept}, duration {duration}"
            )
            self.duration_timer.set_period(duration)
            for topic, val in [
                ("slope", slope),
                ("intercept", intercept),
                ("duration", duration),
                ("profile_i", profile_i),
            ]:
                setattr(state, topic, val)
                self.ps.set(
                    "controller/addition/{0}/{1}".format(self.pump_name, topic), val
                )

        super().update_add_control(state)