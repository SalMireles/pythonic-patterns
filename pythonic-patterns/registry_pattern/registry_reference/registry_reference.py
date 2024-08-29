from abc import ABC, abstractmethod


class Product(ABC):
    pass


class Product1(Product):
    pass


class Product2(Product):
    pass


class AbstractFactory(ABC):
    @abstractmethod
    def create(self) -> Product:
        pass


class ConcreteFactory1(AbstractFactory):
    def create(self) -> Product:
        return Product1()


class ConcreteFactory2(AbstractFactory):
    def create(self) -> Product:
        return Product2()


class Registry:
    def __init__(self):
        self.registry: dict[str, AbstractFactory] = {}

    def register(self, product_type: str, factory: AbstractFactory) -> None:
        self.registry[product_type] = factory

    def unregister(self, product_type: str) -> None:
        self.registry.pop(product_type, None)

    def create(self, product_type: str) -> Product:
        factory = self.registry[product_type]
        return factory.create()


def main() -> None:
    registry = Registry()
    registry.register("product1", ConcreteFactory1())
    registry.register("product2", ConcreteFactory2())

    print(registry.create("product1"))
    print(registry.create("product2"))

    registry.unregister("product1")
    registry.unregister("product2")


if __name__ == "__main__":
    main()
