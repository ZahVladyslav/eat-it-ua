import httpx

from eat_it.models.location import Location


class GeolocationClient:

    def get_location(self):
        response = httpx.get(
            "https://ipapi.co/json/",
            timeout=10,
        )

        response.raise_for_status()

        data = response.json()

        return Location(
            id=None,
            latitude=float(data["latitude"]),
            longitude=float(data["longitude"]),
            city=data.get("city"),
            address=None,
        )