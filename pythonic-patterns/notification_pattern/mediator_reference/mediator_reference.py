from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional


class Mediator(ABC):
    @abstractmethod
    def notify(self, sender: Component):
        pass


class Component(ABC):
    pass


class ConcreteComponent1(Component):
    def __init__(self, mediator: Optional[Mediator]) -> None:
        self.mediator = mediator

    def do_something(self):
        print("ConcreteComponent1.do_something")
        if self.mediator:
            self.mediator.notify(self)


class ConcreteComponent2(Component):
    def __init__(self, mediator: Optional[Mediator]) -> None:
        self.mediator = mediator

    def do_something(self):
        print("ConcreteComponent2.do_something")
        if self.mediator:
            self.mediator.notify(self)


class ConcreteMediator(Mediator):
    def notify(self, sender: Component):
        self.do_something()

    def do_something(self):
        print("ConcreteMediator.do_something")


def main() -> None:
    mediator = ConcreteMediator()
    component1 = ConcreteComponent1(mediator)
    component1.do_something()


if __name__ == "__main__":
    main()
