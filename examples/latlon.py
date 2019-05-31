class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon


class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        super().__init__(lat, lon)
        self.name = name

    def __str__(self):
        return f"{self.name}, {self.lat}, {self.lon}"


class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):
        super().__init__(name, lat, lon)
        self.difficulty = difficulty
        self.size = size

    def new_property_test(self):
        self.new = "Exists"

    def __str__(self):
        return f"{self.name}, diff: {self.difficulty}, size: {self.size}, lat: {self.lat}, lon: {self.lon}"


gc = Geocache("Geo Test", 10, 3, 24, 26)


w = Waypoint("cool", 10, 10)
print(w.name)
print(gc)
