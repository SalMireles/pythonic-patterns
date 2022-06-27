"""
Reflections:

- Pretty similar Protocol
- Some trailer information loss since thos have different brands, models. 
This should have been kept seperate and also would have been best to also
keep car and truck seperate so we can extend their attributes.
- After watching the review video looks like Arjan suggested this was the
correct approach besides keeping Trailer seperate. Keeping Car and Truck 
seperte make sense if their attributes vastly diverge in the future.

- Arjan has a point that the cost assignment can get messy.

"""
from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Protocol


class CostSource(Protocol):
    def compute_cost(self) -> int:
        ...


@dataclass
class DriveDistanceCost:
    km_driven: int
    price_per_km_dollars: int = 5  # maintenance cost

    def compute_cost(self) -> int:
        return self.price_per_km_dollars * self.km_driven


@dataclass
class DailyCost:
    days_rented: int
    price_per_day_dollars: int = 20

    def compute_cost(self) -> int:
        return self.price_per_day_dollars * self.days_rented


@dataclass
class MonthlyCost:
    months_rented: int
    price_per_month_dollars: int = 100

    def compute_cost(self) -> int:
        return self.price_per_month_dollars * self.months_rented


@dataclass
class SeatCost:
    seats: int
    price_per_seat_dollars: int = 50

    def compute_cost(self) -> int:
        return self.price_per_seat_dollars * self.seats


@dataclass
class CapacityCost:
    storage_capacity_liters: int
    price_per_liter_dollars: int = 150

    def compute_cost(self) -> int:
        return self.price_per_liter_dollars * self.storage_capacity_liters


@dataclass
class TrailerCost:
    capacity: int
    price_per_square_feet: int = 150

    def compute_cost(self) -> int:
        return self.price_per_square_feet * self.capacity


@dataclass
class VehicleCapacityCost:
    capacity_m3: int
    price_per_m3_dollars: int = 150
    price_per_month_dollars: int = 200

    def compute_cost(self) -> int:
        return (
            self.price_per_m3_dollars * self.capacity_m3 + self.price_per_month_dollars
        )


class FuelType(Enum):
    PETROL = auto()
    DIESEL = auto()
    ELECTRIC = auto()


class TruckCabStyle(Enum):
    REGULAR = auto()
    EXTENDED = auto()
    CREW = auto()


class RentalType(Enum):
    CAR = auto()
    TRUCK = auto()
    TRAILER = auto()


@dataclass
class Rental:
    brand: str
    model: str
    rental_type: RentalType
    fuel_type: FuelType
    license_plate: str
    reserved: bool
    color: str = None
    cab_style: TruckCabStyle = None
    cost_sources: list[CostSource] = field(default_factory=list)

    def compute_cost(self) -> int:
        return sum(source.compute_cost() for source in self.cost_sources)


def main():
    xyz_capacity_cost = CapacityCost(storage_capacity_liters=100)
    xyz_daily_cost = DailyCost(days_rented=10)
    xyz_seat_cost = SeatCost(seats=4)
    xyz_km_cost = DriveDistanceCost(km_driven=500)

    xyz_rental = Rental(
        brand="toyota",
        model="corolla",
        rental_type=RentalType.CAR,
        color="black",
        fuel_type=FuelType.ELECTRIC,
        license_plate="xyz",
        reserved=True,
        cost_sources=[xyz_capacity_cost, xyz_daily_cost, xyz_seat_cost, xyz_km_cost],
    )
    print(
        f"rental with plate {xyz_rental.license_plate} costs {xyz_rental.compute_cost()} dollars"
    )


if __name__ == "__main__":
    main()
