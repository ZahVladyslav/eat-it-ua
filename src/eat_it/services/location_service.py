from eat_it.repositories.location_repository import LocationRepository


class LocationService:

    def __init__(self):
        self.repository = LocationRepository()

    def create_location(
        self,
        latitude: float,
        longitude: float,
        city: str | None = None,
        address: str | None = None,
    ):
        return self.repository.create(
            latitude=latitude,
            longitude=longitude,
            city=city,
            address=address,
        )

    def get_location_by_id(self, location_id: int):
        return self.repository.get_by_id(location_id)