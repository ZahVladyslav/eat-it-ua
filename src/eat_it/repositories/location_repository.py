from eat_it.database.database import get_connection
from eat_it.models.location import Location


class LocationRepository:

    def create(
        self,
        postal_code: str,
        city: str,
        address: str,
        latitude: float,
        longitude: float,
    ):
        with get_connection() as connection:
            cursor = connection.execute(
                """
                INSERT INTO locations (
                    postal_code,
                    city,
                    address,
                    latitude,
                    longitude
                )
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    postal_code,
                    city,
                    address,
                    latitude,
                    longitude,
                ),
            )

            return cursor.lastrowid

    def get_by_id(self, location_id: int):
        with get_connection() as connection:
            cursor = connection.execute(
                """
                SELECT
                    id,
                    postal_code,
                    city,
                    address,
                    latitude,
                    longitude,
                    created_at
                FROM locations
                WHERE id = ?
                """,
                (location_id,),
            )

            row = cursor.fetchone()

            if row is None:
                return None

            return Location(
                id=row[0],
                postal_code=row[1],
                city=row[2],
                address=row[3],
                latitude=row[4],
                longitude=row[5],
                created_at=row[6],
            )

    def get_by_postal_code(self, postal_code: str):
        with get_connection() as connection:
            cursor = connection.execute(
                """
                SELECT
                    id,
                    postal_code,
                    city,
                    address,
                    latitude,
                    longitude,
                    created_at
                FROM locations
                WHERE postal_code = ?
                """,
                (postal_code,),
            )

            row = cursor.fetchone()

            if row is None:
                return None

            return Location(
                id=row[0],
                postal_code=row[1],
                city=row[2],
                address=row[3],
                latitude=row[4],
                longitude=row[5],
                created_at=row[6],
            )