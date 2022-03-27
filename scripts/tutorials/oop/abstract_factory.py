from abc import ABC, abstractmethod


class Pet(ABC):
    def __init__(self, name: str) -> str:
        self.name = name

    @abstractmethod
    def speak(self):
        pass

    def __str__(self):
        return str(self.name)

class Dog(Pet):
    def __init__(self, name: str) -> str:
        super().__init__(name)

    def speak(self):
        return "grrrr"

class Cat(Pet):
    def __init__(self, name: str) -> str:
        super().__init__(name)

    def speak(self):
        return "meow"
    
    
