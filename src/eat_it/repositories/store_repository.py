from eat_it.database.database import get_connection
from eat_it.models.store import Store


class StoreRepository:

    def create(
        self,
        name: str,
        chain: str,
        address: str,
        city: str,
        latitude: float,
        longitude: float,
        source: str,
        external_id: str,
        store_type: str | None = None,
    ):
        with get_connection() as connection:
            cursor = connection.execute(
                """
                INSERT INTO stores (
                    name,
                    chain,
                    store_type,
                    address,
                    city,
                    latitude,
                    longitude,
                    source,
                    external_id
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    name,
                    chain,
                    store_type,
                    address,
                    city,
                    latitude,
                    longitude,
                    source,
                    external_id,
                ),
            )

            return cursor.lastrowid

    def get_by_id(self, store_id: int):
        with get_connection() as connection:
            cursor = connection.execute(
                """
                SELECT
                    id,
                    name,
                    chain,
                    store_type,
                    address,
                    city,
                    latitude,
                    longitude,
                    source,
                    external_id,
                    created_at
                FROM stores
                WHERE id = ?
                """,
                (store_id,),
            )

            row = cursor.fetchone()

            if row is None:
                return None

            return Store(
                id=row[0],
                name=row[1],
                chain=row[2],
                store_type=row[3],
                address=row[4],
                city=row[5],
                latitude=row[6],
                longitude=row[7],
                source=row[8],
                external_id=row[9],
                created_at=row[10],
            )

    def get_by_external_id(self, external_id: str):
        with get_connection() as connection:
            cursor = connection.execute(
                """
                SELECT
                    id,
                    name,
                    chain,
                    store_type,
                    address,
                    city,
                    latitude,
                    longitude,
                    source,
                    external_id,
                    created_at
                FROM stores
                WHERE external_id = ?
                """,
                (external_id,),
            )

            row = cursor.fetchone()

            if row is None:
                return None

            return Store(
                id=row[0],
                name=row[1],
                chain=row[2],
                store_type=row[3],
                address=row[4],
                city=row[5],
                latitude=row[6],
                longitude=row[7],
                source=row[8],
                external_id=row[9],
                created_at=row[10],
            )

    def get_all(self):
        with get_connection() as connection:
            cursor = connection.execute(
                """
                SELECT
                    id,
                    name,
                    chain,
                    store_type,
                    address,
                    city,
                    latitude,
                    longitude,
                    source,
                    external_id,
                    created_at
                FROM stores
                ORDER BY name
                """
            )

            rows = cursor.fetchall()

            return [
                Store(
                    id=row[0],
                    name=row[1],
                    chain=row[2],
                    store_type=row[3],
                    address=row[4],
                    city=row[5],
                    latitude=row[6],
                    longitude=row[7],
                    source=row[8],
                    external_id=row[9],
                    created_at=row[10],
                )
                for row in rows
            ]