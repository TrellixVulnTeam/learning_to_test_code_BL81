from __future__ import annotations
from abc import ABC, abstractmethod


class Creator:
    @abstractmethod
    def factory_method(self):
        pass

    def buy_pet(self):
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
    f"{creator.buy_pet()}", end="")

def client_code2():
    """Constructs a Pet Factory based on the user's preferences"""
    
    factories = {
        "cat" : ConcreteCatShop(),
        "dog" : ConcreteDogShop()
    }
    while True:
        factory_type = input("Enter the desired shop type (cat, dog): ")
        if factory_type in factories:
            obj = factories[factory_type]
            print(obj.buy_pet())
        else:
            print("Unknown option.")

if __name__ == '__main__':
    # 1.
    creator = ConcreteCatShop()
    client_code(creator)

    print("\n")

    # 2.
    creators = [ConcreteCatShop(), ConcreteDogShop()]
    for creator in creators:
        client_code(creator)
        print("\n")

    print("\n")
    
    # 3.
    client_code2()