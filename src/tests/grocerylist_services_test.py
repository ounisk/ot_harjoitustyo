import unittest
from services.grocerylist_service import GrocerylistService, ProductAlreadyOnListError, ProductNotOnListError
from entities.grocerylist_entity import Grocerylist
from repositories.grocerylist_repository import grocerylist_repository


class TestGrocerylistService(unittest.TestCase): 
    def setUp(self):
        self.grocerylist_service = GrocerylistService()
        #self.grocerylist = Grocerylist()
        self.grocerylist_service.empty_whole_list()

        self.grocery_item = Grocerylist("milk", 1, "K-market")


    def test_newly_created_list_is_empty(self):
        self.assertEqual(len(self.grocerylist_service.get_products()), 0)


    def test_adding_a_product_and_quantity_is_on_the_list(self):
        self.grocerylist_service.add_product(
            self.grocery_item.product, self.grocery_item.quantity, self.grocery_item.store)
        products = self.grocerylist_service.get_products()
        self.assertEqual((products[0][0], products[0][1], products[0]
                         [2]), ("milk", 1, "K-market"))

    def test_adding_products_and_quantities_are_on_the_list(self):
        self.grocerylist_service.add_product("milk", 2, "K-market")
        self.grocerylist_service.add_product("pineapple", 5, "Lidl")
        products = self.grocerylist_service.get_products()
        self.assertEqual(
            (products[0][0], products[1][1], products[1][2]), ("milk", 5, "Lidl"))


    def test_adding_a_product_already_on_the_list_not_success(self):
        self.grocerylist_service.add_product("milk", 2, "Lidl")
        self.assertRaises(ProductAlreadyOnListError,
                          lambda: self.grocerylist_service.add_product("milk", 2, "Lidl"))


    def test_deleting_a_product(self):
        self.grocerylist_service.add_product("milk", 4, "Lidl")
        self.grocerylist_service.add_product("pineapple", 6, "K-market")
        self.grocerylist_service.delete_product("milk", "Lidl")
        products = self.grocerylist_service.get_products()
        self.assertEqual(
            (products[0][0], products[0][1], products[0][2]), ("pineapple", 6, "K-market"))


    def test_delete_product_not_on_the_list_error(self):
        self.assertRaises(
            ProductNotOnListError, lambda: self.grocerylist_service.delete_product("milk", "Lidl"))


    def test_empty_whole_list(self):
        self.grocerylist_service.add_product("milk", 7, "Lidl")
        self.grocerylist_service.add_product("pineapple", 6, "K-market")
        self.grocerylist_service.empty_whole_list()
        products = self.grocerylist_service.get_products()
        self.assertEqual(len(products), 0)


    def test_get_products_per_store(self):
        self.grocerylist_service.add_product("milk", 7, "Lidl")
        self.grocerylist_service.add_product("choco", 3, "Lidl")
        self.grocerylist_service.add_product("beer", 6, "K-market")
        self.grocerylist_service.add_product("sausage", 6, "K-market")
        products1 = self.grocerylist_service.get_products_store("Lidl")
        products2 = self.grocerylist_service.get_products_store("K-market")
        self.assertEqual((products1[0][0], products1[1][0]), ("milk", "choco"))
        self.assertEqual(
            (products2[0][0], products2[1][0]), ("beer", "sausage"))


    def test_modify_quantity(self):
        self.grocerylist_service.add_product("milk", 4, "Lidl")
        self.grocerylist_service.modify_quantity("milk", 234, "Lidl")
        products = self.grocerylist_service.get_products_store("Lidl")
        self.assertEqual(products[0][1], 234)


    def test_modify_quantity_product_not_on_list(self):
        self.grocerylist_service.add_product("milk", 4, "Lidl")
        self.assertRaises(
            ProductNotOnListError, lambda: self.grocerylist_service.modify_quantity("beer", 6, "Lidl"))


    def test_get_top3_products(self):
        grocerylist_repository.empty_history()
        self.grocerylist_service.add_product("milk", 1, "K-market")
        self.grocerylist_service.add_product("milk", 4, "Lidl")
        self.grocerylist_service.add_product("choco", 3, "Lidl")
        top3 = self.grocerylist_service.get_top3_products()
        self.assertEqual((top3[0][0], top3[1][0]), ("milk", "choco"))
