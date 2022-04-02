from __future__ import annotations
from abc import ABC, abstractmethod


class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self):
        product = self.factory_method()
        result = f'Creator: The same creators code has just worked with {product.operation()}'
        return result

class ConcreteCreator1(Creator):
    def factory_method(self) -> Product: #tricky -> Product
        return ConcreteProduct1()

class ConcreteCreator2(Creator):
    def factory_method(self) -> Product: # tricky -> Product
        return ConcreteProduct2()

class Product(ABC):
    @abstractmethod
    def operation(self):
        pass

class ConcreteProduct1(Product):
    def operation(self):
        return "{Result of the ConcreteProduct1}"

class ConcreteProduct2(Product):
    def operation(self):
        return "{Result of the ConcreteProduct2}"

def read_factory(obj_type: str) -> Creator:
    factories = {
        "cc1" : ConcreteCreator1(),
        "cc2" : ConcreteCreator2()
    }
    return factories[obj_type]

def client_code(creator: Creator):
    print(
        f'Client: Im not aware of the creators class, but it still works.\n'
        f'{creator.some_operation()}'
    )

if __name__ == '__main__':
    print("App: Launched with ConcreteCreator1.")
    creator = ConcreteCreator1()
    client_code(creator)

    print("\n")

    print("App: Launced with ConcreteCreator2.")
    creator = ConcreteCreator2()
    client_code(creator)

    print("\n")

    factory = read_factory("cc1")
    client_code(factory)