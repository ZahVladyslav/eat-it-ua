from unittest.mock import Mock, patch

from eat_it.clients.google_places_client import GooglePlacesClient


def test_search_nearby():
    mock_response = Mock()

    mock_response.json.return_value = {
        "places": [
            {
                "id": "place_123",
                "displayName": {
                    "text": "АТБ-Маркет"
                },
                "formattedAddress": "Львів, вул. Тестова, 1",
                "location": {
                    "latitude": 49.8397,
                    "longitude": 24.0297,
                },
                "primaryType": "supermarket",
            }
        ]
    }

    mock_response.raise_for_status.return_value = None

    with patch(
        "eat_it.clients.google_places_client.httpx.post",
        return_value=mock_response,
    ) as mock_post:
        client = GooglePlacesClient()

        result = client.search_nearby(
            latitude=49.8397,
            longitude=24.0297,
        )

    assert len(result["places"]) == 1
    assert result["places"][0]["id"] == "place_123"
    assert result["places"][0]["displayName"]["text"] == "АТБ-Маркет"

    mock_post.assert_called_once()
