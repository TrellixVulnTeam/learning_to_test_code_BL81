from scripts.mapmaker import location


def test_location():
    assert location.location() == "location"