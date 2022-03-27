from abc import ABC, abstractmethod
from typing import Optional, Type, List

"""
An implementation of the Abstract Factory Design Pattern.
What is this pattern about?
In Java and other languages, the Abstract Factory Pattern serves to provide an interface for creating related/dependent objects without the need to specify their actual class.

*TL;DR
Provides a way to encapsulate a group of individual factories.
"""

class Pet(ABC):
    """
    Abstract Product A.
    """
    def __init__(self, name: str) -> str:
        self.name = name

    @abstractmethod
    def speak(self):
        pass


class Dog(Pet):
    """
    Concrete Product A.
    """
    def __init__(self, name: str) -> str:
        super().__init__(name)

    def speak(self):
        return "grrrr"

    def __str__(self):
        return f'Dog<{self.name}>'

class Cat(Pet):
    """
    Concrete Product B.
    """
    def __init__(self, name: str) -> str:
        super().__init__(name)

    def speak(self):
        return "meow"

    def __str__(self):
        return f'Cat<{self.name}>'
    
class PetShopAbstractFactory(ABC):
    """
    The Abstract Factory 
    """
    def __init__(self, animal_factory: Type[Pet]) -> None:
        self.pet_factory = animal_factory

    @abstractmethod
    def buy_pet(self, name: str) -> Pet:
        pass

    def __str__(self):
        return f'type: {self.__class__}'

class PetShopConcreteFactory(PetShopAbstractFactory):
    """
    Concrete Factory
    """
    def __init__(self, animal_factory: Type[Pet]) -> None:
        self.pet_factory = animal_factory

    def buy_pet(self, name: str) -> Pet:
        pet = self.pet_factory(name)
        print(f'Here is your lovely {pet}')
        return pet
    
if __name__ == "__main__":
    cat_shop = PetShopConcreteFactory(Cat)
    print(cat_shop)
    pet = cat_shop.buy_pet("Lucy")
    print(pet.speak())
    
    print("=" * 50)

    dog_shop = PetShopConcreteFactory(Dog)
    print(dog_shop)
    pet = dog_shop.buy_pet("Alvin")
    print(pet.speak())