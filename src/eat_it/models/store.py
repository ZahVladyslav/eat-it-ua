from dataclasses import dataclass


@dataclass
class Store:
    id: int | None
    name: str
    chain: str | None
    address: str | None
    city: str | None
    latitude: float
    longitude: float
    source: str | None
    external_id: str | None
    created_at: str | None = None
    store_type: str | None = None