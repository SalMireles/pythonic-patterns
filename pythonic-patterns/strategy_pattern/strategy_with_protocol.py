""" Using protocols for abstractions.

What did we do?
- Use protocols to abstract away the discount mechanism for orders.
- Rather than inheritance we rely on pythons ducktyping mechanism
- Same as abc. Choose whether you want inheritance vs reliance on ducktyping
- Later on we will learn how to decide between the two.

"""

from dataclasses import dataclass
from typing import Protocol

class DiscountStrategy(Protocol):
    def compute(self, price: int) -> int:
        """Compute the discount for the given price"""


class PercentageDiscount:
    def compute(self, price: int) -> int:
        return int(price * 0.20)


class FixedDiscount:
    def compute(self, price: int) -> int:
        return 10_00


@dataclass
class Order:
    price: int
    quantity: int
    discount: DiscountStrategy

    def compute_total(self) -> int:
        discount = self.discount.compute(self.price * self.quantity)
        return max(0, self.price * self.quantity - discount)


def main() -> None:
    order = Order(price=100_00, quantity=2, discount=PercentageDiscount())
    print(order)
    print(f"Total: ${order.compute_total() / 100:.2f}")


if __name__ == "__main__":
    main()