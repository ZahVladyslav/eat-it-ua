from eat_it.models.shopping_list_item import ShoppingListItem
from eat_it.repositories.shopping_list_item_repository import (
    ShoppingListItemRepository,
)
from eat_it.repositories.shopping_list_repository import ShoppingListRepository


def test_create_shopping_list_item():
    shopping_list_repository = ShoppingListRepository()
    item_repository = ShoppingListItemRepository()

    shopping_list_id = shopping_list_repository.create(
        name="Продукти",
    )

    item_id = item_repository.create(
        shopping_list_id=shopping_list_id,
        product_name="Молоко",
        quantity=2,
        unit="л",
    )

    assert item_id is not None


def test_get_shopping_list_item_by_id():
    shopping_list_repository = ShoppingListRepository()
    item_repository = ShoppingListItemRepository()

    shopping_list_id = shopping_list_repository.create(
        name="Сніданок",
    )

    item_id = item_repository.create(
        shopping_list_id=shopping_list_id,
        product_name="Яйця",
        quantity=10,
        unit="шт",
    )

    item = item_repository.get_by_id(item_id)

    assert isinstance(item, ShoppingListItem)
    assert item.product_name == "Яйця"
    assert item.quantity == 10
    assert item.unit == "шт"


def test_get_items_by_shopping_list():
    shopping_list_repository = ShoppingListRepository()
    item_repository = ShoppingListItemRepository()

    shopping_list_id = shopping_list_repository.create(
        name="Вечеря",
    )

    item_repository.create(
        shopping_list_id=shopping_list_id,
        product_name="Курка",
        quantity=1,
        unit="кг",
    )

    item_repository.create(
        shopping_list_id=shopping_list_id,
        product_name="Рис",
        quantity=2,
        unit="шт",
    )

    items = item_repository.get_by_shopping_list(shopping_list_id)

    assert len(items) == 2
    assert all(isinstance(item, ShoppingListItem) for item in items)


def test_delete_shopping_list_item():
    shopping_list_repository = ShoppingListRepository()
    item_repository = ShoppingListItemRepository()

    shopping_list_id = shopping_list_repository.create(
        name="Тимчасовий список",
    )

    item_id = item_repository.create(
        shopping_list_id=shopping_list_id,
        product_name="Хліб",
    )

    item_repository.delete(item_id)

    item = item_repository.get_by_id(item_id)

    assert item is None