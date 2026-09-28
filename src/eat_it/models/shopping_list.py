from dataclasses import dataclass


@dataclass
class ShoppingList:
    id: int | None
    name: str
    location_id: int | None
    budget: int | None
    created_at: str | None = None
    updated_at: str | None = None