import pytest
import random
from typing import Type

# (venv) (base) batman@the-bank:~/Desktop/learning_to_test_code$ python -m pytest tests/gists/oop/ -vv

class Pet:
    """This could be ABC"""
    def __init__(self, name: str) -> None:
        self.name = name

    def speak(self) -> None:
        raise NotImplementedError
    
    def __str__(self):
        raise NotImplementedError
    
class Dog(Pet):
    """
    NOTE: No super().__init__(name) for Pet
    """
    def speak(self) -> None:
        print("woof")
    
    def __str__(self):
        return f"Dog<{self.name}>"

class Cat(Pet):
    """
    NOTE: No super().__init__(name) for Pet
    """
    def speak(self):
        print("meow")
        
    def __str__(self):
        return f"Cat<{self.name}>"
    
class PetShop:
    """A pet shop"""
    def __init__(self, animal_factory: Type[Pet]) -> None:
        """
        pet_factory is our abstract factory. We can set it at will.
        """
        self.pet_pactory = animal_factory
    
    def buy_pet(self, name: str) -> Pet:
        """
        Creates and shows a pet using the abstract factory
        """
        pet = self.pet_pactory(name)
        print(f"Here is your lovely {pet}")
        return pet

def random_animal(name: str) -> Pet:
    """Lets be dynamic!"""
    return random.choice([Dog, Cat])(name)


def main() -> None:
    cat_shop = PetShop(Cat)
    pet = cat_shop.buy_pet("Lucy")
    pet.speak()


if __name__ == "__main__":
    main()