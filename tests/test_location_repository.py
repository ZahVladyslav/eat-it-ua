from eat_it.models.location import Location
from eat_it.repositories.location_repository import LocationRepository


def test_create_location():
    repository = LocationRepository()

    location_id = repository.create(
        postal_code="79000",
        city="Львів",
        address="площа Ринок",
        latitude=49.8419,
        longitude=24.0315,
    )

    assert location_id is not None


def test_get_location_by_id():
    repository = LocationRepository()

    location_id = repository.create(
        postal_code="79001",
        city="Львів",
        address="проспект Свободи",
        latitude=49.8429,
        longitude=24.0266,
    )

    location = repository.get_by_id(location_id)

    assert isinstance(location, Location)
    assert location.postal_code == "79001"
    assert location.city == "Львів"
    assert location.latitude == 49.8429