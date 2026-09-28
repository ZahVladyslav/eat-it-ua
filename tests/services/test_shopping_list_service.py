from eat_it.models.shopping_list import ShoppingList
from eat_it.models.shopping_list_item import ShoppingListItem
from eat_it.services.shopping_list_service import ShoppingListService


def test_create_list():
    service = ShoppingListService()

    shopping_list_id = service.create_list(
        name="Продукти на тиждень",
        budget=2000,
    )

    assert shopping_list_id is not None


def test_get_list_by_id():
    service = ShoppingListService()

    shopping_list_id = service.create_list(
        name="Сніданки",
        budget=1000,
    )

    shopping_list = service.get_list_by_id(shopping_list_id)

    assert isinstance(shopping_list, ShoppingList)
    assert shopping_list.name == "Сніданки"
    assert shopping_list.budget == 1000


def test_get_all_lists():
    service = ShoppingListService()

    service.create_list(name="Продукти")

    shopping_lists = service.get_all_lists()

    assert isinstance(shopping_lists, list)
    assert all(
        isinstance(shopping_list, ShoppingList)
        for shopping_list in shopping_lists
    )


def test_delete_list():
    service = ShoppingListService()

    shopping_list_id = service.create_list(
        name="Тимчасовий список"
    )

    service.delete_list(shopping_list_id)

    shopping_list = service.get_list_by_id(shopping_list_id)

    assert shopping_list is None


def test_create_list_with_negative_budget():
    service = ShoppingListService()

    try:
        service.create_list(
            name="Неправильний список",
            budget=-100,
        )
        assert False
    except ValueError:
        assert True


def test_add_item():
    service = ShoppingListService()

    shopping_list_id = service.create_list(
        name="Продукти"
    )

    item_id = service.add_item(
        shopping_list_id=shopping_list_id,
        product_name="Молоко",
        quantity=2,
        unit="л",
    )

    assert item_id is not None


def test_get_items():
    service = ShoppingListService()

    shopping_list_id = service.create_list(
        name="Вечеря"
    )

    service.add_item(
        shopping_list_id=shopping_list_id,
        product_name="Курка",
        quantity=1,
        unit="кг",
    )

    service.add_item(
        shopping_list_id=shopping_list_id,
        product_name="Рис",
        quantity=2,
        unit="шт",
    )

    items = service.get_items(shopping_list_id)

    assert len(items) == 2
    assert all(isinstance(item, ShoppingListItem) for item in items)


def test_delete_item():
    service = ShoppingListService()

    shopping_list_id = service.create_list(
        name="Тимчасовий список"
    )

    item_id = service.add_item(
        shopping_list_id=shopping_list_id,
        product_name="Хліб",
    )

    service.delete_item(item_id)

    items = service.get_items(shopping_list_id)

    assert len(items) == 0


def test_empty_product_name():
    service = ShoppingListService()

    shopping_list_id = service.create_list(
        name="Продукти"
    )

    try:
        service.add_item(
            shopping_list_id=shopping_list_id,
            product_name="",
        )
        assert False
    except ValueError:
        assert True


def test_invalid_quantity():
    service = ShoppingListService()

    shopping_list_id = service.create_list(
        name="Продукти"
    )

    try:
        service.add_item(
            shopping_list_id=shopping_list_id,
            product_name="Молоко",
            quantity=0,
        )
        assert False
    except ValueError:
        assert True