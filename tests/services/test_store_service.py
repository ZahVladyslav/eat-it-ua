from eat_it.models.store import Store
from eat_it.services.store_service import StoreService


def test_create_store():
    service = StoreService()

    store_id = service.create_store(
        name="АТБ",
        chain="АТБ",
        address="вул. Городоцька, 10",
        city="Львів",
        latitude=49.8397,
        longitude=24.0297,
        source="test",
        external_id="atb_service_test_1",
    )

    assert store_id is not None


def test_get_store_by_id():
    service = StoreService()

    store_id = service.create_store(
        name="Сільпо",
        chain="Сільпо",
        address="вул. Стрийська, 20",
        city="Львів",
        latitude=49.8200,
        longitude=24.0200,
        source="test",
        external_id="silpo_service_test_1",
    )

    store = service.get_store_by_id(store_id)

    assert isinstance(store, Store)
    assert store.name == "Сільпо"
    assert store.chain == "Сільпо"


def test_get_store_by_external_id():
    service = StoreService()

    service.create_store(
        name="Рукавичка",
        chain="Рукавичка",
        address="вул. Шевченка, 30",
        city="Львів",
        latitude=49.8500,
        longitude=24.0100,
        source="test",
        external_id="rukavychka_service_test_1",
    )

    store = service.get_store_by_external_id(
        "rukavychka_service_test_1"
    )

    assert isinstance(store, Store)
    assert store.name == "Рукавичка"


def test_get_all_stores():
    service = StoreService()

    service.create_store(
        name="АТБ",
        chain="АТБ",
        address="вул. Тестова, 1",
        city="Львів",
        latitude=49.8397,
        longitude=24.0297,
        source="test",
        external_id="atb_service_test_2",
    )

    stores = service.get_all_stores()

    assert isinstance(stores, list)
    assert all(isinstance(store, Store) for store in stores)


def test_empty_store_name():
    service = StoreService()

    try:
        service.create_store(
            name="",
            chain="АТБ",
            address="вул. Тестова, 1",
            city="Львів",
            latitude=49.8397,
            longitude=24.0297,
            source="test",
            external_id="invalid_store",
        )
        assert False
    except ValueError:
        assert True


def test_empty_store_city():
    service = StoreService()

    try:
        service.create_store(
            name="АТБ",
            chain="АТБ",
            address="вул. Тестова, 1",
            city="",
            latitude=49.8397,
            longitude=24.0297,
            source="test",
            external_id="invalid_store_2",
        )
        assert False
    except ValueError:
        assert True