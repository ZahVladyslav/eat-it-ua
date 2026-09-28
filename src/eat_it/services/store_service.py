from eat_it.models.store import Store
from eat_it.repositories.store_repository import StoreRepository
from eat_it.utils.geo import calculate_distance


class StoreService:

    def __init__(self):
        self.repository = StoreRepository()

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
    ):
        if not name:
            raise ValueError("Назва магазину не може бути порожньою.")

        if not city:
            raise ValueError("Місто не може бути порожнім.")

        return self.repository.create(
            name=name,
            chain=chain,
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