from scripts.mapmaker.mapmaker_start import Point

def test_one_point():
    p1 = Point("Pleasanton", 20.5, 30.5)
    assert p1.get_lat_long() == (20.5, 30.5)
    assert p1.get_city() == "Pleasanton"
    assert p1.__str__() == f"Created a new city: {p1.city} with an object of type {Point.__name__}"