
class Point:
    def __init__(self, city, lat, long):
        self.city = city
        self.lat = lat
        self.long = long

    def get_lat_long(self):
        return (self.lat, self.long)

    def get_city(self):
        return self.city

    # to be readable by a human
    def __str__(self):
        return f"Created a new city: {self.city} with an object of type {Point.__name__}"

    # to be unambiguous even if "machine like" and gives all information about object
    def __repr__(self):
        return f"This is __repr__() of an object of class {Point.__name__}"

p1 = Point("Pleasanton", 20.5, 30.5)
print(str(p1))
print(repr(p1))

