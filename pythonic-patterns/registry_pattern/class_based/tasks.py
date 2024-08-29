from dataclasses import dataclass
from typing import Any

from registry import Task


@dataclass
class Pulse:
    strength: int

    def run(self) -> None:
        print(
            f"Sending a subspace pulse of {self.strength} microPicards to the converter assembly."
        )


@dataclass
class Recalibrate:
    target: str

    def run(self) -> None:
        print(f"Recalibrating the {self.target}.")


@dataclass
class Reinforce:
    plating_type: str
    target: str

    def run(self) -> None:
        print(f"Reinforcing {self.plating_type} plating of {self.target}.")


class PulseFactory:
    def create(self, args: dict[str, Any]) -> Task:
        return Pulse(**args)


class RecalibrateFactory:
    def create(self, args: dict[str, Any]) -> Task:
        return Recalibrate(**args)


class ReinforceFactory:
    def create(self, args: dict[str, Any]) -> Task:
        return Reinforce(**args)
