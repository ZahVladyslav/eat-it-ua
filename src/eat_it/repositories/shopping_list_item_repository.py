from eat_it.database.database import get_connection


class ShoppingListItemRepository:

    def create(
        self,
        shopping_list_id: int,
        product_name: str,
        quantity: float = 1,
        unit: str | None = None,
    ):
        with get_connection() as connection:
            cursor = connection.execute(
                """
                INSERT INTO shopping_list_items (
                    shopping_list_id,
                    product_name,
                    quantity,
                    unit
                )
                VALUES (?, ?, ?, ?)
                """,
                (
                    shopping_list_id,
                    product_name,
                    quantity,
                    unit,
                ),
            )

            return cursor.lastrowid

    def get_by_id(self, item_id: int):
        with get_connection() as connection:
            cursor = connection.execute(
                """
                SELECT
                    id,
                    shopping_list_id,
                    product_name,
                    quantity,
                    unit
                FROM shopping_list_items
                WHERE id = ?
                """,
                (item_id,),
            )

            return cursor.fetchone()

    def get_by_shopping_list(self, shopping_list_id: int):
        with get_connection() as connection:
            cursor = connection.execute(
                """
                SELECT
                    id,
                    shopping_list_id,
                    product_name,
                    quantity,
                    unit
                FROM shopping_list_items
                WHERE shopping_list_id = ?
                ORDER BY id
                """,
                (shopping_list_id,),
            )

            return cursor.fetchall()

    def delete(self, item_id: int):
        with get_connection() as connection:
            connection.execute(
                """
                DELETE FROM shopping_list_items
                WHERE id = ?
                """,
                (item_id,),
            )