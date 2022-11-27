from entities.grocerylist_entity import Grocerylist
from repositories.grocerylist_repository import (
    grocerylist_repository as default_grocerylist_repository)


class GrocerylistService:

    def __init__(self, grocerylist_repository=default_grocerylist_repository):
        #self._groceries = []
        self._grocerylist_repository = grocerylist_repository

    def add_product(self, product: str):
        list_products = self._grocerylist_repository.list_products()

        for products in list_products:
            if products.product == product:
                print("Tuote on jo listalla")
                return

            # else:
        product = Grocerylist(product=product)  # , quantity=2)

        return self._grocerylist_repository.add(product)
        # return

    def delete_product(self, product):  # added 22.11
        #list_products = self._grocerylist_repository.list_products()

        # for products in list_products:
        #    if not products.product == product:
        #        print("Tuotetta ei ole listalla!")
        #        return

        self._grocerylist_repository.delete(product)

    def empty_whole_list(self):  # added 26.11
        self._grocerylist_repository.empty_all()

    def get_products(self):
        # if not self._groceries:
        #    return None
        # else:
        # palauttaa objekteja!!!!  vai a=self._kauppalista.... ja return list(a)
        return self._grocerylist_repository.list_products()


grocerylist_service = GrocerylistService()


# BELOW old code before repository architecture change:
# class Grocerylist:   #OLD code, before repository architecture
#    def __init__(self):
#        self._groceries = []

#    def add_product(self, product: str):
#        if product in self._groceries:
#            print("Tuote on jo listalla")
#            return
#        else:
#            self._groceries.append(product)
# return

#    def delete_product(self, product: str):  #added 22.11
#        self._groceries.remove(product)

# add modify function

#    def get_products(self):
#        if not self._groceries:
#            return None
#        else:
#            return self._groceries
