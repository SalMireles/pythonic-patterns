import dataclasses
from typing import List, Optional


@dataclasses.dataclass
class AdditionSchedule:
    rates: List[float]
    volumes: List[float]
    efts: List[float]

    def __post_init__(self):
        if not all(len(lst) == len(self.efts) for lst in [self.rates, self.volumes]):
            raise ValueError(f"{self.__class__.__name__}: Lists are not of equal length.")

    def get_schedule(self):
        return [
            {
                "addition_rate": self.rates[index],
                "addition_volume": self.volumes[index],
                "addition_eft": self.efts[index],
            }
            for index, _ in enumerate(self.efts)
        ]

def start_bolus_feed(topic: str, addition_schedule: AdditionSchedule):
    """
    Output: [{'start_rate': 0.0045, 'end_rate': 0.019, 'duration': 20160.0}, 
            {'start_rate': 0.019, 'end_rate': 0.021, 'duration': 3600.0}, 
            {'start_rate': 0.021, 'end_rate': 0.021, 'duration': 360000.0}
    ]
    """
    schedule = addition_schedule.get_schedule()
    print(schedule)
    print(len(schedule))
    profile_i = 0
    slope, intercept, duration = schedule[profile_i]["addition_rate"], schedule[profile_i]["addition_volume"], schedule[profile_i]["addition_eft"],
    for topic, val in [
                ("slope", slope),
                ("intercept", intercept),
                ("duration", duration),
                ("profile_i", profile_i),
            ]:
            print(topic, val)



if __name__ == "__main__":
    test_schedule = AdditionSchedule(rates=[1.0, 1.0], volumes=[1, 2], efts=[1, 2])
    start_bolus_feed(topic="hello", addition_schedule=test_schedule)