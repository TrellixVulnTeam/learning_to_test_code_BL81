class Person:
    def __init__(self, name: str, age: int, *args, **kwargs) -> str: 
        self.name = name
        self.age = age

    def __str__(self):
        return str(self.name)
    
class Employee(Person):
    def __init__(self, name: str, age: int, role: str, *args, **kwargs) -> str:
        super().__init__(name, age)
        self.role = role
    
    def address_team(self):
        return "Hello team!"
    
if __name__ == "__main__":
    args_list = ["alice", 50]
    args_dict = {"name" : "alice", "age" : 50}
    
    p1 = Person(*args_list)
    p2 = Person(**args_dict)
    print(p1)
    print(p2)
    
    emp_list = ["dave", 50, "editor"]
    emp_dict = {"name" : "dave", "age" : 50, "role" : "editor"}
    e1 = Employee(*emp_list)
    e2 = Employee(**emp_dict)
    print(e1)
    print(e2)