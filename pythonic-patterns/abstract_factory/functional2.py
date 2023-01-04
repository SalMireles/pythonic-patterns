from functools import partial
from typing import Callable, Optional

IncomeTaxCalculator = Callable[[int, Optional[bool]], int]
CapitalTaxCalculator = Callable[[int], int]
TaxFactory = tuple[IncomeTaxCalculator, CapitalTaxCalculator]


def calculate_tax_on_rate(base: int, tax_rate: float = 0.1) -> int:
    return int(base * tax_rate)


def calculate_income_tax_nl(income: int, apply_floor=True) -> int:
    floor = 10_000_00
    brackets: list[tuple[int | None, float]] = [
        (69_398_00, 0.37),
        (None, 0.495),
    ]
    taxable_income = income
    if apply_floor:
        taxable_income -= floor

    total_tax = 0
    for max_income, percentage in brackets:
        bracket_income = min(taxable_income, max_income or taxable_income)
        total_tax += int(bracket_income * percentage)
        taxable_income -= bracket_income
        if taxable_income <= 0:
            break
    return total_tax


calculate_zero_tax = partial(calculate_tax_on_rate, tax_rate=0)

simple_tax_factory: TaxFactory = (
    partial(calculate_tax_on_rate, tax_rate=0.1),
    calculate_zero_tax,
)

nl_tax_factory: TaxFactory = (
    calculate_income_tax_nl,
    partial(calculate_tax_on_rate, tax_rate=0.05),
)


def compute_tax(
    factory: TaxFactory, income: int, capital: int, apply_floor: bool = True
) -> int:
    """Computes tax for a given income and capital."""
    income_tax_calculator, capital_tax_calculator = factory

    # calculate the tax
    income_tax = income_tax_calculator(income, apply_floor)
    capital_tax = capital_tax_calculator(capital)

    # return the total tax
    return income_tax + capital_tax


def main():
    # compute the tax
    income = 100_000_00
    capital = 100_000_00
    tax = compute_tax(nl_tax_factory, income, capital)
    print(
        f"Tax for income ${income/100:.2f} and capital ${capital/100:.2f} is ${tax/100:.2f}."
    )


if __name__ == "__main__":
    main()
