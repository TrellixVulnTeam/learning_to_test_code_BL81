from scripts.mapmaker.challenge1 import Point
import pytest

def test_make_one_point():
    p1 = Point("Dakar", 14.7167, 17.4677)
    assert p1.get_lat_long() == (14.7167, 17.4677)


def test_invalid_point_generation():
    with pytest.raises(Exception) as exp:
        Point("Senegal", 99.6937, -189.44406)
    # breakpoint()
    #assert str(exp.value) == "Invalid lat, longitude combination."
