# This script demonstrates the differences between static methods and class methods.
# KZ 1-15-22

from datetime import date, datetime, time, timedelta


class Person:
    def __init__(self, name: str, age: int) -> str:
        self.name = name
        self.age = age
    
    @classmethod
    def fromBirthYear(cls, name: str, year: int):
        return cls(name, date.today().year - year)
    
    @staticmethod
    def isAdult(age: int) -> bool:
        return age >= 18
    
    def __str__(self):
        return str(self.name)


class Employee( Person ):
    pass
    