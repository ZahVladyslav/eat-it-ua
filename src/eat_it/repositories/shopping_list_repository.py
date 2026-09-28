from eat_it.database.database import get_connection
from eat_it.models.shopping_list import ShoppingList


class ShoppingListRepository:

    def create(
        self,
        name: str,
        location_id: int | None = None,
        budget: int | None = None,
    ):
        with get_connection() as connection:
            cursor = connection.execute(
                """
                INSERT INTO shopping_lists (
                    name,
                    location_id,
                    budget
                )
                VALUES (?, ?, ?)
                """,
                (
                    name,
                    location_id,
                    budget,
                ),
            )

            return cursor.lastrowid

    def get_by_id(self, shopping_list_id: int):
        with get_connection() as connection:
            cursor = connection.execute(
                """
                SELECT
                    id,
                    name,
                    location_id,
                    budget,
                    created_at,
                    updated_at
                FROM shopping_lists
                WHERE id = ?
                """,
                (shopping_list_id,),
            )

            row = cursor.fetchone()

            if row is None:
                return None

            return ShoppingList(
                id=row[0],
                name=row[1],
                location_id=row[2],
                budget=row[3],
                created_at=row[4],
                updated_at=row[5],
            )

    def get_all(self):
        with get_connection() as connection:
            cursor = connection.execute(
                """
                SELECT
                    id,
                    name,
                    location_id,
                    budget,
                    created_at,
                    updated_at
                FROM shopping_lists
                ORDER BY created_at DESC
                """
            )

            rows = cursor.fetchall()

            return [
                ShoppingList(
                    id=row[0],
                    name=row[1],
                    location_id=row[2],
                    budget=row[3],
                    created_at=row[4],
                    updated_at=row[5],
                )
                for row in rows
            ]

    def delete(self, shopping_list_id: int):
        with get_connection() as connection:
            connection.execute(
                """
                DELETE FROM shopping_lists
                WHERE id = ?
                """,
                (shopping_list_id,),
            )