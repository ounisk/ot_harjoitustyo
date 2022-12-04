#from pathlib import Path
from entities.grocerylist_entity import Grocerylist
from database_connection import get_database_connection
#from config import ALIST_FILE_PATH


class GrocerylistRepository:
    def __init__(self, connection):
        self._connection = connection

    def list_products(self):
        cursor = self._connection.cursor()
        #cursor.execute("SELECT * FROM Groceries")
        cursor.execute(
            "SELECT product, quantity, store FROM Groceries ORDER BY store")
        rows = cursor.fetchall()

        products = []

        for row in rows:
            products.append(row)
        return products
        # if rows:
        #    return list([Grocerylist(row["product"], row["quantity"]) for row in rows])
        # else:
        #    return None

    def list_products_store(self, in_store):  # added 2.12
        cursor = self._connection.cursor()
        cursor.execute(
            """SELECT product, quantity FROM Groceries WHERE store =(?)""", [in_store])
        rows = cursor.fetchall()

        if rows:
            products = []

            for row in rows:
                products.append(row)
            return products

    def find_product(self, find_product, in_store):
        cursor = self._connection.cursor()
        #cursor.execute("SELECT product FROM Groceries WHERE product = ?", [find_product])
        cursor.execute("SELECT product FROM Groceries WHERE product = (?) AND store =(?)",
                       [find_product, in_store])
        rows = cursor.fetchall()

        products = []

        for row in rows:
            products.append(row)
        return products
        # vaihtoehto(kurssipruju):
        # return [Grocerylist(row["product"], row["quantity"]) for row in rows]

    def add(self, new_product: Grocerylist):
        cursor = self._connection.cursor()
        cursor.execute("INSERT INTO Groceries (product, quantity, store) VALUES (?,?, ?)",
                       [new_product.product, new_product.quantity, new_product.store])
        self._connection.commit()

    def delete(self, product_delete, from_store):
        cursor = self._connection.cursor()
        cursor.execute("SELECT id FROM Groceries WHERE product = (?) AND store =(?)",
                       [product_delete, from_store])

        del_id = cursor.fetchone()[0]
        cursor.execute("DELETE FROM Groceries WHERE id = (?)", [del_id])
        self._connection.commit()

    def empty_all(self):
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM Groceries")
        self._connection.commit()


grocerylist_repository = GrocerylistRepository(get_database_connection())
