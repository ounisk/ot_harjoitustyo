from entities.grocerylist_entity import Grocerylist
from repositories.grocerylist_repository import (
    grocerylist_repository as default_grocerylist_repository)


class ProductAlreadyOnListError(Exception):
    pass


class ProductNotOnListError(Exception):
    pass


class GrocerylistService:

    def __init__(self, grocerylist_repository=default_grocerylist_repository):
        #self._groceries = []
        self._grocerylist_repository = grocerylist_repository

    def add_product(self, product: str, quantity: int, store: str):
        # Database
        product_is_on_list = self._grocerylist_repository.find_product(
            product, store)

        if product_is_on_list:
            raise ProductAlreadyOnListError("Tuote on jo listalla!")

        # list_products = self._grocerylist_repository.list_products() #CSV:lle
        # for products in list_products:
        #    if products.product == product:
        #        print("Tuote on jo listalla")
        #        return
            # else:
        product = Grocerylist(product=product, quantity=quantity, store=store)

        return self._grocerylist_repository.add(product)
        # return

    def delete_product(self, product, store):
        try:  # lisätty try except 4.12.2022
            self._grocerylist_repository.delete(product, store)
        except TypeError:
            raise ProductNotOnListError("Tuotetta ei ole listalla!")

    def empty_whole_list(self):
        self._grocerylist_repository.empty_all()

    def get_products(self):
        return self._grocerylist_repository.list_products()

    def get_products_store(self, store):  # lis 2.12
        return self._grocerylist_repository.list_products_store(store)


grocerylist_service = GrocerylistService()
