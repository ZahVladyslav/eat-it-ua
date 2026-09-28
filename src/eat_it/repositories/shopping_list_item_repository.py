from eat_it.database.database import get_connection
from eat_it.models.shopping_list_item import ShoppingListItem


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

            row = cursor.fetchone()

            if row is None:
                return None

            return ShoppingListItem(
                id=row[0],
                shopping_list_id=row[1],
                product_name=row[2],
                quantity=row[3],
                unit=row[4],
            )

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

            rows = cursor.fetchall()

            return [
                ShoppingListItem(
                    id=row[0],
                    shopping_list_id=row[1],
                    product_name=row[2],
                    quantity=row[3],
                    unit=row[4],
                )
                for row in rows
            ]

    def delete(self, item_id: int):
        with get_connection() as connection:
            connection.execute(
                """
                DELETE FROM shopping_list_items
                WHERE id = ?
                """,
                (item_id,),
            )