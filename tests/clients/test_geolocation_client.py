from unittest.mock import Mock, patch

from eat_it.clients.geolocation_client import GeolocationClient
from eat_it.models.location import Location


def test_get_location():
    mock_response = Mock()

    mock_response.json.return_value = {
        "latitude": 49.8397,
        "longitude": 24.0297,
        "city": "Lviv",
    }

    mock_response.raise_for_status.return_value = None

    with patch(
        "eat_it.clients.geolocation_client.httpx.get",
        return_value=mock_response,
    ):
        client = GeolocationClient()

        location = client.get_location()

    assert isinstance(location, Location)
    assert location.latitude == 49.8397
    assert location.longitude == 24.0297
    assert location.city == "Lviv"
    assert location.address is None