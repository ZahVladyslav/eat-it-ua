from eat_it.database.database import get_connection


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
    ):
        with get_connection() as connection:
            cursor = connection.execute(
                """
                INSERT INTO stores (
                    name,
                    chain,
                    address,
                    city,
                    latitude,
                    longitude,
                    source,
                    external_id
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    name,
                    chain,
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

            return cursor.fetchone()

    def get_by_external_id(self, external_id: str):
        with get_connection() as connection:
            cursor = connection.execute(
                """
                SELECT
                    id,
                    name,
                    chain,
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

            return cursor.fetchone()

    def get_all(self):
        with get_connection() as connection:
            cursor = connection.execute(
                """
                SELECT
                    id,
                    name,
                    chain,
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

            return cursor.fetchall()