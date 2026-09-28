from eat_it.models.store import Store
from eat_it.repositories.store_repository import StoreRepository


def test_create_store():
    repository = StoreRepository()

    store_id = repository.create(
        name="АТБ",
        chain="АТБ",
        address="вул. Городоцька, 10",
        city="Львів",
        latitude=49.8397,
        longitude=24.0297,
        source="test",
        external_id="atb_test_1",
    )

    assert store_id is not None


def test_get_store_by_id():
    repository = StoreRepository()

    store_id = repository.create(
        name="Сільпо",
        chain="Сільпо",
        address="вул. Стрийська, 20",
        city="Львів",
        latitude=49.8200,
        longitude=24.0200,
        source="test",
        external_id="silpo_test_1",
    )

    store = repository.get_by_id(store_id)

    assert isinstance(store, Store)
    assert store.name == "Сільпо"
    assert store.chain == "Сільпо"
    assert store.city == "Львів"


def test_get_store_by_external_id():
    repository = StoreRepository()

    repository.create(
        name="Рукавичка",
        chain="Рукавичка",
        address="вул. Шевченка, 30",
        city="Львів",
        latitude=49.8500,
        longitude=24.0100,
        source="test",
        external_id="rukavychka_test_1",
    )

    store = repository.get_by_external_id("rukavychka_test_1")

    assert isinstance(store, Store)
    assert store.name == "Рукавичка"


def test_get_all_stores():
    repository = StoreRepository()

    stores = repository.get_all()

    assert isinstance(stores, list)
    assert all(isinstance(store, Store) for store in stores)