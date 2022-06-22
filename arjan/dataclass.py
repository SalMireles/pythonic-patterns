import random
import string
from dataclasses import dataclass, field
from enum import Enum, auto
from typing import List


def generate_vehicle_license() -> str:
    """Helper method for generating a vehicle license number."""

    digit_part = "".join(random.choices(string.digits, k=2))
    letter_part_1 = "".join(random.choices(string.ascii_uppercase, k=2))
    letter_part_2 = "".join(random.choices(string.ascii_uppercase, k=2))
    return f"{letter_part_1}-{digit_part}-{letter_part_2}"


class Accessory(Enum):
    AIRCO = auto()
    CRUISECONTROL = auto()
    NAVIGATION = auto()
    OPENROOF = auto()
    BATHTUB = auto()
    MINIBAR = auto()


class FuelType(Enum):
    PETROL = auto()
    DIESEL = auto()
    ELECTRIC = auto()


@dataclass  # (frozen=True) - block instance updates after init
class Vehicle:
    brand: str
    model: str
    color: str
    # license_plate: str = field(
    #     default_factory=generate_vehicle_license, init=False
    # )  # prevent instance setting
    license_plate: str = field(
        init=False
    )  # using post init to generate based on condition
    fuel_type: FuelType = FuelType.ELECTRIC
    # by default dataclasses don't allow passing mutable objects but can get around it
    # by using default_factory. Expects a function that returns an object of specified type
    # def default_foo():
    # return [Accessory.AIRCO]
    # default_factory=default_foo
    accessories: List[Accessory] = field(
        default_factory=lambda: [Accessory.AIRCO, Accessory.NAVIGATION]
    )

    def __post_init__(self):
        # use for more complicated init attributes
        # doesn't work if dc is frozen
        self.license_plate = generate_vehicle_license()
        if self.brand == "Tesla":
            self.license_plate += "-t"

    # def generate_license_plate(self):
    #     self.license_plate = generate_vehicle_license()


def main() -> None:
    """
    Create some vehicles and print their details.
    """

    tesla = Vehicle(
        brand="Tesla",
        model="Model 3",
        color="black",
        # license_plate=generate_vehicle_license(),
        accessories=[
            Accessory.AIRCO,
            Accessory.MINIBAR,
            Accessory.NAVIGATION,
            Accessory.CRUISECONTROL,
        ],
    )
    volkswagen = Vehicle(
        brand="Volkswagen",
        model="ID3",
        color="white",
        # license_plate=generate_vehicle_license(),
        accessories=[Accessory.AIRCO, Accessory.NAVIGATION],
    )
    bmw = Vehicle(
        brand="BMW",
        model="520e",
        color="blue",
        # license_plate=generate_vehicle_license(),
        fuel_type=FuelType.PETROL,
        accessories=[Accessory.NAVIGATION, Accessory.CRUISECONTROL],
    )

    print(tesla)
    print(volkswagen)
    print(bmw)


if __name__ == "__main__":
    main()
