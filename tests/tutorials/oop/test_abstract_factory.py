from scripts.tutorials.oop.abstract_factory import Pet, Dog, Cat
import unittest

class TestDog(unittest.TestCase):
    def test_dog_barks(self):
        dog = Dog("tim")
        assert dog.name == "tim"
        assert dog.speak() == "grrrr"

class TestCat(unittest.TestCase):
    def test_cat_meows(self):
        cat = Cat("alice")
        assert cat.name == "alice"
        assert cat.speak() == "meow"