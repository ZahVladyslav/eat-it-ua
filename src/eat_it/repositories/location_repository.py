from eat_it.database.database import get_connection
from eat_it.models.location import Location


class LocationRepository:

    def create(
        self,
        latitude: float,
        longitude: float,
        city: str | None = None,
        address: str | None = None,
    ):
        with get_connection() as connection:
            cursor = connection.execute(
                """
                INSERT INTO locations (
                    city,
                    address,
                    latitude,
                    longitude
                )
                VALUES (?, ?, ?, ?)
                """,
                (
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
                city=row[1],
                address=row[2],
                latitude=row[3],
                longitude=row[4],
                created_at=row[5],
            )