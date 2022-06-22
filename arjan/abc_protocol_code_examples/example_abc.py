import math
from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime


class Vehicle(ABC):
    @abstractmethod  # enforces that you can't make an instance of vehicle
    def reserve(self, start_date: datetime, days: int):
        """A vehicle can be reserved for renting"""

    @abstractmethod
    def renew_license(self, new_license_date: datetime):
        """Renews the license of a vehicle."""


@dataclass
class Car(Vehicle):
    model: str
    reserved: bool = False

    def reserve(self, start_date: datetime, days: int):
        self.reserved = True
        print(f"Reserving car {self.model} for {days} days at date {start_date}.")

    def renew_license(self, new_license_date: datetime):
        print(f"Renewing license of car {self.model} to {new_license_date}.")


@dataclass
class Truck(Vehicle):
    model: str
    reserved: bool = False
    reserved_trailer: bool = False

    def reserve(self, start_date: datetime, days: int):
        months = math.ceil(days / 30)
        self.reserved = True
        self.reserved_trailer = True
        print(
            f"Reserving truck {self.model} for {months} month(s) at date {start_date}, including a trailer."
        )

    def renew_license(self, new_license_date: datetime):
        print(f"Renewing license of truck {self.model} to {new_license_date}.")


# not in the dataclass
def reserve_now(vehicle: Vehicle):
    # each vehicle has it's own implementation of the reserve method
    vehicle.reserve(datetime.now(), 40)


def main():
    car = Car("Ford")
    truck = Truck("DAF")
    reserve_now(car)
    reserve_now(truck)


if __name__ == "__main__":
    main()
