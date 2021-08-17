
class Point:
    def __init__(self, city, lat, long):
        self.city = city
    
        if not (-90 <= lat <= 90) or not (-180 <= long <= 180):
            raise ValueError("Invalid latitude, longitude combination")
            self.lat = lat
            self.long = long

    # if not (-90 <= self.lat <= 90) or not (-180 <= long <= 180):
    #     raise ValueError("Invalid latitude, longitude combination")

    def get_lat_long(self):
        return (self.lat, self.long)

p1 = Point("Pleasanton", -200.5, 30.5)
print(p1.get_lat_long())