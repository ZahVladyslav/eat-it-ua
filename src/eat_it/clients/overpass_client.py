import httpx


class OverpassClient:

    BASE_URL = "https://overpass.private.coffee/api/interpreter"

    def __init__(self):
        self.timeout = 30
        self.headers = {
            "User-Agent": "eat_it/0.1.0",
            "Accept": "application/json",
        }

    def search_nearby_stores(
        self,
        latitude: float,
        longitude: float,
        radius_m: int = 1000,
    ):
        query = f"""
        [out:json];

        nwr(
            around:{radius_m},
            {latitude},
            {longitude}
        )[shop];

        out center;
        """

        response = httpx.get(
            self.BASE_URL,
            params={"data": query},
            headers=self.headers,
            timeout=60,
        )

        response.raise_for_status()

        elements = response.json()["elements"]

        food_stores = [
            element
            for element in elements
            if element.get("tags", {}).get("shop") in FOOD_SHOP_TYPES
        ]

        return food_stores