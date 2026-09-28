from eat_it.clients.google_places_client import GooglePlacesClient
from eat_it.models.store import Store
from eat_it.repositories.store_repository import StoreRepository
from eat_it.utils.geo import calculate_distance


class StoreService:

    def __init__(self):
        self.repository = StoreRepository()
        self.google_places_client = GooglePlacesClient()

    def create_store(
        self,
        name: str,
        chain: str,
        address: str,
        city: str,
        latitude: float,
        longitude: float,
        source: str,
        external_id: str,
        store_type: str | None = None,
    ):
        if not name:
            raise ValueError("Назва магазину не може бути порожньою.")

        if not city:
            raise ValueError("Місто не може бути порожнім.")

        return self.repository.create(
            name=name,
            chain=chain,
            store_type=store_type,
            address=address,
            city=city,
            latitude=latitude,
            longitude=longitude,
            source=source,
            external_id=external_id,
        )

    def get_store_by_id(self, store_id: int):
        return self.repository.get_by_id(store_id)

    def get_store_by_external_id(self, external_id: str):
        return self.repository.get_by_external_id(external_id)

    def get_all_stores(self):
        return self.repository.get_all()

    def get_nearby_stores(
        self,
        latitude: float,
        longitude: float,
        radius_km: float = 1.0,
    ):
        if radius_km <= 0:
            raise ValueError("Радіус повинен бути більшим за 0.")

        stores = self.repository.get_all()

        nearby_stores = []

        for store in stores:
            distance = calculate_distance(
                latitude,
                longitude,
                store.latitude,
                store.longitude,
            )

            if distance <= radius_km:
                nearby_stores.append(
                    (store, distance)
                )

        nearby_stores.sort(
            key=lambda item: item[1]
        )

        return nearby_stores

    def search_nearby_stores(
        self,
        latitude: float,
        longitude: float,
        radius_km: float = 1.0,
    ):
        if radius_km <= 0:
            raise ValueError("Радіус повинен бути більшим за 0.")

        response = self.google_places_client.search_nearby(
            latitude=latitude,
            longitude=longitude,
            radius=radius_km * 1000,
        )

        allowed_types = {
            "supermarket",
            "grocery_store",
            "convenience_store",
        }

        stores = []

        for place in response.get("places", []):
            primary_type = place.get("primaryType")

            if primary_type not in allowed_types:
                continue

            location = place.get("location", {})
            display_name = place.get("displayName", {})

            store = Store(
                id=None,
                name=display_name.get("text", "Без назви"),
                chain=None,
                store_type=primary_type,
                address=place.get("formattedAddress"),
                city=None,
                latitude=location.get("latitude"),
                longitude=location.get("longitude"),
                source="google_places",
                external_id=place.get("id"),
            )

            stores.append(store)

        return stores