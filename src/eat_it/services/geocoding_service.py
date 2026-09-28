from eat_it.clients.nominatim_client import NominatimClient


class GeocodingService:

    def __init__(self):
        self.client = NominatimClient()

    def geocode_postal_code(self, postal_code: str):

        if not postal_code:
            raise ValueError("Поштовий індекс не може бути порожнім.")

        results = self.client.search_by_postal_code(
            postal_code
        )

        if not results:
            return None

        result = results[0]

        return {
            "postal_code": postal_code,
            "city": result.get("address", {}).get("city")
            or result.get("address", {}).get("town")
            or result.get("address", {}).get("village"),
            "address": result.get("display_name"),
            "latitude": float(result["lat"]),
            "longitude": float(result["lon"]),
        }