
class Point:
    def __init__(self, city, lat, long):
        self._city = city
        self._lat = lat
        self._long = long

    def get_lat_long(self):
        return (self._lat, self._long)

    def get_city(self):
        return self._city

    def __str__(self):
        return f"Created a new city: {self._city}"