from abc import ABC, abstractmethod


class ProductA(ABC):
    pass


class ProductB(ABC):
    pass


class ProductA1(ProductA):
    pass


class ProductA2(ProductA):
    pass


class ProductB1(ProductB):
    pass


class ProductB2(ProductB):
    pass


class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self) -> ProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> ProductB:
        pass


class ConcreteFactory1(AbstractFactory):
    def create_product_a(self) -> ProductA:
        return ProductA1()

    def create_product_b(self) -> ProductB:
        return ProductB1()


class ConcreteFactory2(AbstractFactory):
    def create_product_a(self) -> ProductA:
        return ProductA2()

    def create_product_b(self) -> ProductB:
        return ProductB2()


def main():
    factory = ConcreteFactory1()
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()
    print(product_a)
    print(product_b)


if __name__ == "__main__":
    main()
