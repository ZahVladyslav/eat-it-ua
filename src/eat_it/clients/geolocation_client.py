import httpx


class GeolocationClient:

    def get_location(self):
        response = httpx.get(
            "https://ipapi.co/json/",
            timeout=10,
        )

        response.raise_for_status()

        data = response.json()

        return {
            "latitude": float(data["latitude"]),
            "longitude": float(data["longitude"]),
            "city": data.get("city"),
            "address": None,
        }