
class Point():
    def __init__(self, name, lat, long):
        self.name = name
        self.lat = lat
        self.long = long

        if not (-90 <= lat <= 90) or not (-180 <= long <= 180):
            raise ValueError("Invalid lat, longitude combination.")

    def get_lat_long(self):
        return (self.lat, self.long)
