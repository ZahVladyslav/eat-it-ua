from eat_it.clients.overpass_client import OverpassClient


client = OverpassClient()

stores = client.search_nearby_stores(
    latitude=49.8365397,
    longitude=24.0383982,
    radius_m=1000,
)

print(f"Знайдено: {len(stores)}")

for store in stores:
    print(
        store.get("tags", {}).get("name"),
        store.get("tags", {}).get("shop"),
    )