import os

import httpx
from dotenv import load_dotenv


load_dotenv()


class GooglePlacesClient:

    URL = "https://places.googleapis.com/v1/places:searchNearby"

    def __init__(self):
        self.api_key = os.getenv("GOOGLE_PLACES_API_KEY")

        if not self.api_key:
            raise ValueError(
                "GOOGLE_PLACES_API_KEY is not set"
            )

    def search_nearby(
        self,
        latitude: float,
        longitude: float,
        radius: float = 1000,
        max_results: int = 20,
    ):
        response = httpx.post(
            self.URL,
            headers={
                "Content-Type": "application/json",
                "X-Goog-Api-Key": self.api_key,
                "X-Goog-FieldMask": (
                    "places.id,"
                    "places.displayName,"
                    "places.formattedAddress,"
                    "places.location,"
                    "places.primaryType"
                ),
            },
            json={
                "includedTypes": [
                    "supermarket",
                    "grocery_store",
                    "convenience_store",
                ],
                "maxResultCount": max_results,
                "rankPreference": "DISTANCE",
                "locationRestriction": {
                    "circle": {
                        "center": {
                            "latitude": latitude,
                            "longitude": longitude,
                        },
                        "radius": radius,
                    }
                },
            },
            timeout=10,
        )

        response.raise_for_status()

        return response.json()