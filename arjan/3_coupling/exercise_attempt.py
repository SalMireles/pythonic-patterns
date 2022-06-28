"""
CODE NOT WORKING - Incomplete after 1 hr.


Notes:
- We have a dictionary that relies on a data class to create 3 Vehicle data instances
then we rely on the the dictionary to check if the keys are valid. If valid we pass
this string to a function to compute a total cost by refering to the specific instance
found in the dictionary.

- Seems like this dictionary should just belong to the class and the read_vehicle_type()
compute_rental_cost() should be a method

- Current thought is to create an enum class and use this  

- Ooh how about a method to add the data to the class and the class can
contain the methods that rely on the data. Use an alternative constructor via
a classmethod (something cool I learned recently.)

- Outcome: Spend ~1hr and didn't land on a solution so proceeding so will proceed.

- My solution was to add the vehicle data to a dataclass then was going to use 
that to perform operations. This seemed way too nested.

- Lesson: For some reason I tried to redifine the dictionary and that spiraled
out of control. The apprach was to still use it but pass it in as an arg
where needed and to move change functions that related to a class as a method.

"""
from dataclasses import dataclass, field
from enum import Enum


class VehicleBrands(Enum):
    VW = "vw"
    BMW = "bmw"
    FORD = "ford"


VEHICLE_DATA = {
    VehicleBrands.VW: {"price_per_km": 30, "price_per_day": 6000},
    VehicleBrands.BMW: {"price_per_km": 35, "price_per_day": 8500},
    VehicleBrands.FORD: {"price_per_km": 25, "price_per_day": 12000},
}


@dataclass
class VehicleData:
    """A class to hold vehicle data."""

    price_per_day: int
    price_per_km: int
    brand: str = None
    days_rented: int = None
    km_driven: int = None


@dataclass
class VehicleDatabase:
    "A class to hold all vehicle data"
    km_price: dict[str, int] = field(default_factory=dict)
    daily_price: dict[str, int] = field(default_factory=dict)

    def add_vehicle_data(self, vehicle_dict):
        for key, values in vehicle_dict.items():
            self.km_price[key].append(values.get("price_per_km"))
            self.daily_price[key].append(values.get("price_per_day"))


def read_vehicle_type() -> str:
    """Reads the vehicle type from the user."""
    vehicle_type = ""
    while vehicle_type not in VEHICLE_DATA:
        vehicle_type = input(
            f"What type of vehicle would you like to rent ({', '.join(VEHICLE_DATA)})? "
        )
    return vehicle_type


def read_rent_days() -> int:
    """Reads the number of days from the user."""
    days = 0
    while days < 1:
        days_str = input(
            "How many days would you like to rent the vehicle? (enter a positive number) "
        )
        try:
            days = int(days_str)
        except ValueError:
            print("Invalid input. Please enter a number.")
    return days


def read_kms_to_drive() -> int:
    """Reads the number of kilometers to drive from the user."""
    km = 0
    while km < 1:
        km_str = input(
            "How many kilometers would you like to drive (enter a positive number)? "
        )
        try:
            km = int(km_str)
        except ValueError:
            print("Invalid input. Please enter a number.")
    return km


def main():

    vehicle_type = read_vehicle_type()

    days = read_rent_days()

    km = read_kms_to_drive()

    # compute the final rental price
    rental_price = compute_rental_cost(vehicle_type, days, km)

    # print the result
    print(f"The total price of the rental is ${(rental_price / 100):.2f}")


if __name__ == "__main__":
    main()
