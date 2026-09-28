from dataclasses import dataclass


@dataclass
class ShoppingListItem:
    id: int | None
    shopping_list_id: int
    product_name: str
    quantity: float
    unit: str | None