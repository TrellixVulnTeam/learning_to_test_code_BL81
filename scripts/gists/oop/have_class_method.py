


class Cat:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        
    @classmethod
    def from_cat_years(cls, name, cat_years):
        return cls(name, cat_years//7)

    def purr(self): 
        return "meow"