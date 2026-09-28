from eat_it.services.location_service import LocationService
from unittest.mock import Mock
from eat_it.models.location import Location


def test_get_current_location():
    service = LocationService()

    service.geolocation_client = Mock()

    service.geolocation_client.get_location.return_value = Location(
        id=None,
        latitude=49.8397,
        longitude=24.0297,
        city="Lviv",
        address=None,
    )

    location = service.get_current_location()

    assert isinstance(location, Location)
    assert location.latitude == 49.8397
    assert location.longitude == 24.0297
    assert location.city == "Lviv"
    assert location.address is None

def test_create_location(test_database):
    service = LocationService()

    location_id = service.create_location(
        latitude=49.8397,
        longitude=24.0297,
        city="Львів",
        address="площа Ринок",
    )

    assert location_id is not None


def test_get_location_by_id(test_database):
    service = LocationService()

    location_id = service.create_location(
        latitude=49.8397,
        longitude=24.0297,
        city="Львів",
        address="площа Ринок",
    )

    location = service.get_location_by_id(location_id)

    assert location is not None
    assert location.id == location_id
    assert location.city == "Львів"
    assert location.address == "площа Ринок"
    assert location.latitude == 49.8397
    assert location.longitude == 24.0297