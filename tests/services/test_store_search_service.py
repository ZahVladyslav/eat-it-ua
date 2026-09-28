import pytest

from eat_it.services.store_service import StoreService


def test_get_nearby_stores():
    service = StoreService()

    service.create_store(
        name="АТБ",
        chain="АТБ",
        address="вул. Тестова, 1",
        city="Львів",
        latitude=49.8365,
        longitude=24.0384,
        source="test",
        external_id="near_atb",
    )

    service.create_store(
        name="Сільпо",
        chain="Сільпо",
        address="вул. Тестова, 2",
        city="Львів",
        latitude=49.8370,
        longitude=24.0390,
        source="test",
        external_id="near_silpo",
    )

    service.create_store(
        name="Рукавичка",
        chain="Рукавичка",
        address="вул. Тестова, 3",
        city="Львів",
        latitude=50.0000,
        longitude=24.0000,
        source="test",
        external_id="far_rukavychka",
    )

    stores = service.get_nearby_stores(
        latitude=49.8365,
        longitude=24.0384,
        radius_km=1,
    )

    assert len(stores) == 2

    assert stores[0][0].name == "АТБ"
    assert stores[1][0].name == "Сільпо"

    assert stores[0][1] < stores[1][1]


def test_get_nearby_stores_with_small_radius():
    service = StoreService()

    service.create_store(
        name="АТБ",
        chain="АТБ",
        address="вул. Тестова, 1",
        city="Львів",
        latitude=49.8365,
        longitude=24.0384,
        source="test",
        external_id="atb_radius_test",
    )

    stores = service.get_nearby_stores(
        latitude=49.8365,
        longitude=24.0384,
        radius_km=0.01,
    )

    assert len(stores) == 1
    assert stores[0][0].name == "АТБ"


def test_get_nearby_stores_invalid_radius():
    service = StoreService()

    with pytest.raises(ValueError):
        service.get_nearby_stores(
            latitude=49.8365,
            longitude=24.0384,
            radius_km=0,
        )