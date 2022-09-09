""" Using a functional approach for abstraction.

What did we do?
- Callable allows you to use a class with a __call__ dunder method or just use a function
- Option to make percentage_discount to higher order function so it can return a fuction
that can return a function that can compute the total. This is called a CLOSURE (function within a function)
- Shorter method to return a lambda function


"""

from dataclasses import dataclass
from typing import Callable

DiscountFunction = Callable[[int], int]

# lambda approach
# def percentage_discount(percentage: float) -> DiscountFunction:
#     return lambda price: int(price * percentage)

def percentage_discount(percentage: float) -> DiscountFunction:
    def compute_discount(price: int) -> int:
        return int(price * percentage)
    return compute_discount


def fixed_discount(price: int, fixed: int) -> int:
    return fixed


@dataclass
class Order:
    price: int
    quantity: int
    discount: DiscountFunction

    def compute_total(self) -> int:
        discount = self.discount(self.price * self.quantity)
        return max(0, self.price * self.quantity - discount)


def main() -> None:
    order = Order(price=100_00, quantity=2, discount=percentage_discount(0.12))
    print(order)
    print(f"Total: ${order.compute_total() / 100:.2f}")


if __name__ == "__main__":
    main()