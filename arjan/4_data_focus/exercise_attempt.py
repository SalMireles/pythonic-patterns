"""
- See solution on how to decouple total price even further.
"""

from dataclasses import dataclass, field

from enum import Enum, auto


class PaymentStatus(Enum):
    """Payment status"""

    OPEN = auto()
    PAID = auto()


@dataclass
class ItemInfo:
    items: str
    quantities: int
    prices: int


@dataclass
class Order:
    items: list[ItemInfo] = field(default_factory=list)
    status: PaymentStatus = PaymentStatus.OPEN

    def add_item(self, item: ItemInfo) -> None:
        self.items.append(item)

    @property
    def total_price(self) -> int:
        total = 0
        for i in range(len(self.items)):
            total += self.items[i].quantities * self.items[i].prices
        return total


def main() -> None:
    order = Order()
    order.add_item(ItemInfo("Keyboard", 1, 5000))
    order.add_item(ItemInfo("SSD", 1, 15000))
    order.add_item(ItemInfo("USB cable", 2, 500))

    print(f"The total price is: ${(order.total_price / 100):.2f}.")


if __name__ == "__main__":
    main()
