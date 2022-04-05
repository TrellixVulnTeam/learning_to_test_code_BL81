from scripts.tutorials.oop.property_decorator_person import Person
import pytest


class Test:
    def test_init_ok(self):
        p1 = Person(name="kevin", age=30)
        assert p1.name == "kevin"
        assert p1.age == 30
        assert p1.email == "kevin@aol.com"

    def test_property_decorator_works(self):
        p1 = Person(name="kevin", age=30)
        p1.name = "jim"
        assert p1.email == "jim@aol.com"
        assert p1.name == "jim"
        assert p1.age == 30
