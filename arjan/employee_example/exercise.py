"""
Exercise to improve by either using inheritance or composition (using protocols).add()

- Notes:

Vehicle
- metadata + whether reserved

- you can rent a vehicle by either day or month
-- if by day, you pay per day AND per km
-- if by month, you only pay a fixed price

- No matter what rental approach you take. The number of seats and 
storage capacity will will impact the price (naming goes from vehicle to car).

- We have 3 layers of inheritance for all this

CarPerMonth(VehiclePerMonth(Vehicle))

- Truck is a vehicle with an added cab attribute

- You can also rent a Trailer for a certain fixed monthly price based on it's capacity.

--------------------------------------------------------------------------------

How can we improve this code?

- Rent a car and determine rental cost 
- Can only rent if it's not already reserved
- We have prices by km, day, month, seats, storage capacity, and trailers

- We could have a vehicle class with defined type (car or truck) and add costs
with a protocol. The license plate is unique so we have to check if booked by this #.

See exercise_attempt.py for attempt and exercise_solution for more insight.

"""

from dataclasses import dataclass
from enum import Enum, auto


class FuelType(Enum):
    PETROL = auto()
    DIESEL = auto()
    ELECTRIC = auto()


class TruckCabStyle(Enum):
    REGULAR = auto()
    EXTENDED = auto()
    CREW = auto()


@dataclass
class Vehicle:
    brand: str
    model: str
    color: str
    fuel_type: FuelType
    license_plate: str
    reserved: bool


@dataclass
class VehiclePerDay(Vehicle):
    # prices
    price_per_km: int  # weird there is also a price per km
    price_per_day: int


@dataclass
class VehiclePerMonth(Vehicle):
    # prices
    price_per_month: int


@dataclass
class CarPerDay(VehiclePerDay):
    # metadata. Impact pricing?
    number_of_seats: int
    storage_capacity_litres: int


@dataclass
class CarPerMonth(VehiclePerMonth):
    # metadata. Impact pricing?
    number_of_seats: int
    storage_capacity_litres: int


@dataclass
class Truck(Vehicle):
    cab_style: TruckCabStyle


@dataclass
class Trailer:
    brand: str
    model: str
    capacity_m3: int
    price_per_month: int
    reserved: bool


def main():
    pass


if __name__ == "__main__":
    main()
