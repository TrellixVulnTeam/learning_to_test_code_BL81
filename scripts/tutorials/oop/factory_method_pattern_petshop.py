from __future__ import annotations
from abc import ABC, abstractmethod


class Creator:
    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self):
        # sourcery skip: inline-immediately-returned-variable
        product = self.factory_method()
        result = f"Creator: The same creator's code has just worked with {product.speak()}"        
        return result
        

class ConcreteDogShop(Creator):
    def factory_method(self) -> Dog: # tricky
        return Dog()

class ConcreteCatShop(Creator):
    def factory_method(self) -> Cat: # tricky
        return Cat()

class Pet(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Pet):
    def speak(self):
        return "*woof*"

class Cat(Pet):
    def speak(self):
        return "*meow*"

def client_code(creator: Creator):
    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
    f"{creator.some_operation()}", end="")

if __name__ == '__main__':
    creators = [ConcreteCatShop(), ConcreteDogShop()]
    for creator in creators:
        client_code(creator)
        print("\n")