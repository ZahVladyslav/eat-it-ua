from eat_it.models.shopping_list import ShoppingList
from eat_it.repositories.shopping_list_repository import ShoppingListRepository


def test_create_shopping_list():
    repository = ShoppingListRepository()

    shopping_list_id = repository.create(
        name="Продукти на тиждень",
        budget=2000,
    )

    assert shopping_list_id is not None


def test_get_shopping_list_by_id():
    repository = ShoppingListRepository()

    shopping_list_id = repository.create(
        name="Сніданки",
        budget=1000,
    )

    shopping_list = repository.get_by_id(shopping_list_id)

    assert isinstance(shopping_list, ShoppingList)
    assert shopping_list.name == "Сніданки"
    assert shopping_list.budget == 1000


def test_get_all_shopping_lists():
    repository = ShoppingListRepository()

    shopping_lists = repository.get_all()

    assert isinstance(shopping_lists, list)
    assert all(
        isinstance(shopping_list, ShoppingList)
        for shopping_list in shopping_lists
    )


def test_delete_shopping_list():
    repository = ShoppingListRepository()

    shopping_list_id = repository.create(
        name="Тимчасовий список",
    )

    repository.delete(shopping_list_id)

    shopping_list = repository.get_by_id(shopping_list_id)

    assert shopping_list is None