# https://refactoring.guru/design-patterns/builder/python/example
# Builder in Python

"""
Definition:

Builder is a creational design pattern, which allows constructing compelx objects step by step.

  - Unlike other creational patterns, Builder doesn't require products to have a common interface. 
  - That makes it possible to produce different products using the same construction process.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class Builder(ABC):
    """
    The Builder interface specifies methods for creating the different parts of the Product objects.
    """
    pass

class ConcreteBuilder1(Builder):
    pass

class Product1:
    pass

class Director:
    pass


if __name__ == "__main__":
    pass