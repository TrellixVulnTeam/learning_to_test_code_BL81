from scripts.tutorials.oop.static_vs_class_methods import Person, Employee
from datetime import date, datetime, time, timedelta


class TestPerson:

    def test_constructor(self):
        person1 = Person("Al", 70)
        assert ("Al", 70) == (person1.name, person1.age)
        
    def test_isAdult(self):
        # static method
        assert Person.isAdult(20) == True
        assert Person.isAdult(18) == True
        assert Person.isAdult(16) == False
        
    def test_fromBirthYear(self):
        # classmethod
        person1 = Person.fromBirthYear("Al", 1985)
        assert (person1.name, person1.age) == ("Al", 37) 
        
# class TestEmployee:
    
#     def test_constructor(self):
#         emp1 = Employee("Tim", 60, "Broadcaster")
#         assert ("Tim", 60, "Broadcaster") == (emp1.name, emp1.age, emp1.role)
                