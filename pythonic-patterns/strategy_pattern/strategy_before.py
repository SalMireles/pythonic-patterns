""" Before implementing the strategy pattern approach.

What's wrong here?
- ifs are not maintainable and will be complex if discount expands
- some magic numbers are present that would be difficult to modify

what should we do instead?
- Enum the discount
- Implement the strategy pattern

"""

from dataclasses import dataclass


@dataclass
class Order:
    price: int
    quantity: int

    def compute_total(self, discount_type: str) -> int:
        if discount_type == "percentage":
            discount = int(self.price * self.quantity * 0.20)
        elif discount_type == "fixed":
            discount = 10_00
        else:
            discount = 0
        return max(0, self.price * self.quantity - discount)


def main() -> None:
    order = Order(price=100_00, quantity=2)
    print(order)
    print(f"Total: ${order.compute_total('percentage')/100:.2f}")