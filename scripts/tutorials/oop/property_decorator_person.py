# Cory Schaefar Property Decorator Example
# KZ 4-4-22

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # self.email = f"{self.name}@aol.com" # replace with property decorator b/c will break if you change name
        
    @property
    def email(self):
        return f"{self.name}@aol.com"

    def __str__(self):
        return f"<Person>{self.name}"
    
if __name__ == '__main__':
    p1 = Person("kevin", 30)
    p1.name = "jim"
    print(p1.email)