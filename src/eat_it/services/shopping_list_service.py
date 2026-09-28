from eat_it.models.shopping_list import ShoppingList
from eat_it.models.shopping_list_item import ShoppingListItem
from eat_it.repositories.shopping_list_item_repository import (
    ShoppingListItemRepository,
)
from eat_it.repositories.shopping_list_repository import ShoppingListRepository


class ShoppingListService:

    def __init__(self):
        self.list_repository = ShoppingListRepository()
        self.item_repository = ShoppingListItemRepository()

    def create_list(
        self,
        name: str,
        location_id: int | None = None,
        budget: int | None = None,
    ):
        if not name:
            raise ValueError("Назва списку не може бути порожньою.")

        if budget is not None and budget < 0:
            raise ValueError("Бюджет не може бути від'ємним.")

        return self.list_repository.create(
            name=name,
            location_id=location_id,
            budget=budget,
        )

    def get_list_by_id(self, shopping_list_id: int):
        return self.list_repository.get_by_id(shopping_list_id)

    def get_all_lists(self):
        return self.list_repository.get_all()

    def delete_list(self, shopping_list_id: int):
        self.list_repository.delete(shopping_list_id)

    def add_item(
        self,
        shopping_list_id: int,
        product_name: str,
        quantity: float = 1,
        unit: str | None = None,
    ):
        if not product_name:
            raise ValueError("Назва продукту не може бути порожньою.")

        if quantity <= 0:
            raise ValueError("Кількість повинна бути більшою за 0.")

        return self.item_repository.create(
            shopping_list_id=shopping_list_id,
            product_name=product_name,
            quantity=quantity,
            unit=unit,
        )

    def get_items(self, shopping_list_id: int):
        return self.item_repository.get_by_shopping_list(
            shopping_list_id
        )

    def delete_item(self, item_id: int):
        self.item_repository.delete(item_id)