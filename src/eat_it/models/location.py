from dataclasses import dataclass


@dataclass
class Location:
    id: int | None
    postal_code: str
    city: str | None
    address: str | None
    latitude: float
    longitude: float
    created_at: str | None = None