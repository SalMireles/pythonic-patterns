from abc import ABC, abstractmethod
from dataclasses import dataclass


class IncomeTaxCalculator(ABC):
    @abstractmethod
    def calculate_tax(self, income: int, apply_floor=True) -> int:
        """Calculates income tax."""


class CapitalTaxCalculator(ABC):
    @abstractmethod
    def calculate_tax(self, capital: int) -> int:
        """Calculates capital tax."""


@dataclass
class SimpleIncomeTaxCalculator(IncomeTaxCalculator):
    tax_rate: float = 0.1

    def calculate_tax(self, income: int, apply_floor=True) -> int:
        return int(income * self.tax_rate)


@dataclass
class NLTaxCalculator(IncomeTaxCalculator):
    floor: int = 10_000_00

    def calculate_tax(self, income: int, apply_floor=True) -> int:
        brackets: list[tuple[int | None, float]] = [
            (69_398_00, 0.37),
            (None, 0.495),
        ]
        taxable_income = income
        if apply_floor:
            taxable_income -= self.floor

        total_tax = 0
        for max_income, percentage in brackets:
            bracket_income = min(taxable_income, max_income or taxable_income)
            total_tax += int(bracket_income * percentage)
            taxable_income -= bracket_income
            if taxable_income <= 0:
                break
        return total_tax


@dataclass
class PercentageCapitalTaxCalculator(CapitalTaxCalculator):
    tax_rate: float = 0.05

    def calculate_tax(self, capital: int) -> int:
        return int(capital * self.tax_rate)


class ZeroCapitalTaxCalculator(CapitalTaxCalculator):
    def calculate_tax(self, capital: int) -> int:
        return 0


class TaxFactory(ABC):
    @abstractmethod
    def create_income_tax_calculator(self) -> IncomeTaxCalculator:
        """Creates an income tax calculator."""

    @abstractmethod
    def create_capital_tax_calculator(self) -> CapitalTaxCalculator:
        """Creates a capital tax calculator."""


class SimpleTaxFactory(TaxFactory):
    def create_income_tax_calculator(self) -> IncomeTaxCalculator:
        return SimpleIncomeTaxCalculator()

    def create_capital_tax_calculator(self) -> CapitalTaxCalculator:
        return ZeroCapitalTaxCalculator()


class NLTaxFactory(TaxFactory):
    def create_income_tax_calculator(self) -> IncomeTaxCalculator:
        return NLTaxCalculator()

    def create_capital_tax_calculator(self) -> CapitalTaxCalculator:
        return PercentageCapitalTaxCalculator()


def compute_tax(
    factory: TaxFactory, income: int, capital: int, apply_floor: bool = True
) -> int:
    """Computes tax for a given income and capital."""

    # create the calculator
    income_tax_calculator = factory.create_income_tax_calculator()
    capital_tax_calculator = factory.create_capital_tax_calculator()

    # calculate the tax
    income_tax = income_tax_calculator.calculate_tax(income, apply_floor)
    capital_tax = capital_tax_calculator.calculate_tax(capital)

    # return the total tax
    return income_tax + capital_tax


def main():
    # create the factory
    factory = NLTaxFactory()

    # compute the tax
    income = 100_000_00
    capital = 100_000_00
    tax = compute_tax(factory, income, capital)
    print(
        f"Tax for income ${income/100:.2f} and capital ${capital/100:.2f} is ${tax/100:.2f}."
    )


if __name__ == "__main__":
    main()
