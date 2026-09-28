from eat_it.services.store_service import StoreService


service = StoreService()

stores = service.search_nearby_stores(
    latitude=49.8397,
    longitude=24.0297,
    radius_km=1.0,
)

for store in stores:
    print(
        f"{store.name} | "
        f"{store.address} | "
        f"{store.latitude}, {store.longitude} | "
        f"{store.external_id}"
    )