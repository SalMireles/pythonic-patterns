"""
Very advanced Employee management system.

- All we did here is remove commission from each type of employee
and then create another EmployeeTypeWithCommisiion(EmployeeType) class

- Using inheritance in this form didn't really make sense since we have to 
create double the amount of classes to save a bit of code computing pay.

How does using composition help us clean this? (go see that code!)
"""

from dataclasses import dataclass


@dataclass
class HourlyEmployee:
    name: str
    id: int
    # Notice that we got rid of contracts and commisions
    pay_rate: int
    hours_worked: float = 0
    employer_cost: int = 100000

    def compute_pay(self) -> int:
        return int(self.pay_rate * self.hours_worked + self.employer_cost)


@dataclass
class SalariedEmployee:
    name: str
    id: int
    monthly_salary: int
    percentage: float = 1

    def compute_pay(self) -> int:
        return int(self.monthly_salary * self.percentage)


@dataclass
class Freelancer:
    name: str
    id: int
    pay_rate: int
    hours_worked: float = 0
    vat_number: str = ""

    def compute_pay(self) -> int:
        return int(self.pay_rate * self.hours_worked)


@dataclass
class SalariedEmployeeWithCommission(SalariedEmployee):
    commission: int = 10000
    contracts_landed: float = 0

    def compute_pay(self) -> int:
        return super().compute_pay() + int(self.commission * self.contracts_landed)


@dataclass
class HourlyEmployeeWithCommission(HourlyEmployee):
    commission: int = 10000
    contracts_landed: float = 0

    def compute_pay(self) -> int:
        # cool, this is how you use a method from an inherited class
        return super().compute_pay() + int(self.commission * self.contracts_landed)


@dataclass
class FreelancerWithCommission(Freelancer):
    commission: int = 10000
    contracts_landed: float = 0

    def compute_pay(self) -> int:
        return super().compute_pay() + int(self.commission * self.contracts_landed)


def main() -> None:

    henry = HourlyEmployee(name="Henry", id=12346, pay_rate=5000, hours_worked=100)
    print(f"{henry.name} earned ${(henry.compute_pay() / 100):.2f}.")

    sarah = SalariedEmployeeWithCommission(
        name="Sarah", id=47832, monthly_salary=500000, contracts_landed=10
    )
    print(f"{sarah.name} earned ${(sarah.compute_pay() / 100):.2f}.")


if __name__ == "__main__":
    main()
