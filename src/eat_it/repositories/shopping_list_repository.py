from eat_it.database.database import get_connection


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

            return cursor.fetchone()

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

            return cursor.fetchall()

    def delete(self, shopping_list_id: int):
        with get_connection() as connection:
            connection.execute(
                """
                DELETE FROM shopping_lists
                WHERE id = ?
                """,
                (shopping_list_id,),
            )