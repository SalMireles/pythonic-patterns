from __future__ import annotations

from abc import ABC
from typing import Optional


class Handler(ABC):
    def __init__(self):
        self.next: Optional[Handler] = None

    def set_next(self, handler: Handler) -> None:
        self.next = handler

    def handle(self) -> None:
        if self.next:
            self.next.handle()


class ConcreteHandler1(Handler):
    def handle(self) -> None:
        print("ConcreteHandler1.handle")
        return super().handle()


class ConcreteHandler2(Handler):
    def handle(self) -> None:
        print("ConcreteHandler2.handle")
        return super().handle()


def main() -> None:
    concrete_handler1 = ConcreteHandler1()
    concrete_handler2 = ConcreteHandler2()
    concrete_handler2.set_next(concrete_handler1)
    concrete_handler2.handle()


if __name__ == "__main__":
    main()
