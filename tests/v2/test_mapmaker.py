from scripts.v2 import mapmaker


def test_location():
    assert mapmaker.location() == "location"