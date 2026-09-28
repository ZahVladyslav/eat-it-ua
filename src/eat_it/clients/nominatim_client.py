import httpx


class NominatimClient:

    BASE_URL = "https://nominatim.openstreetmap.org/search"

    def __init__(self):
        self.headers = {
            "User-Agent": "eat_it/0.1.0"
        }

    def search_by_postal_code(self, postal_code: str):
        params = {
            "postalcode": postal_code,
            "countrycodes": "ua",
            "format": "jsonv2",
            "addressdetails": 1,
            "limit": 1,
        }

        response = httpx.get(
            self.BASE_URL,
            params=params,
            headers=self.headers,
            timeout=10,
        )

        response.raise_for_status()

        return response.json()