from pathlib import Path
from entities.grocerylist_entity import Grocerylist
from config import ALIST_FILE_PATH


class GrocerylistRepository:
    def __init__(self, file_path):
        self._file_path = file_path

    def list_products(self):
        return self._get_list()

    def _check_file(self):
        Path(self._file_path).touch()

    def _get_list(self):
        tuotteet = []

        self._check_file()
        with open(self._file_path, encoding="utf-8") as file:
            for row in file:
                row = row.replace("\n", "")
                parts = row.split(";")

                product = parts[0]
                #quantity = parts[1]
                #store_id = parts[2]

                # , quantity)) #, store_id))
                tuotteet.append(Grocerylist(product))

        return tuotteet

    def add(self, product):
        tuotteet = self.list_products()
        tuotteet.append(product)
        self._update(tuotteet)
        return product

    def delete(self, product_del):
        #list_products = self.list_products()
        # for product_del in list_products:
        # if list_products.product_del == product_del:
        #    list_products.remove(product_del)  # tämä ei mene oikein!!!!!
        # list_products.remove(product) oli ensin, poisti vääriä tuotteita

        # self._update(list_products)
        # Alternative:
        list_products = self.list_products()

        list_products_without_item = filter(
            lambda grocerylist: grocerylist.product != product_del, list_products)
        self._update(list_products_without_item)

    def empty_all(self):  # added 26.11 empties whole list
        list_products = []
        self._update(list_products)

    def _update(self, tuotteet):
        self._check_file()

        with open(self._file_path, "w", encoding="utf-8") as file:
            for tuote in tuotteet:

                # ;{tuote.quantity}" #;{tuote.store_id}"
                row = f"{tuote.product}"
                file.write(row+"\n")


grocerylist_repository = GrocerylistRepository(ALIST_FILE_PATH)
