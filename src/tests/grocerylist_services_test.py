import unittest
from services.grocerylist_service import GrocerylistService, ProductAlreadyOnListError, ProductNotOnListError
from ui.ui import Grocerylist_app
from entities.grocerylist_entity import Grocerylist


class TestGrocerylist_app(unittest.TestCase):
    def setUp(self):
        self.grocerylist_app = Grocerylist_app()
        self.grocerylist_service = GrocerylistService()
        #self.grocerylist = Grocerylist()

        self.grocery_item = Grocerylist("milk", 1, "K-market")

    def test_newly_created_list_is_empty(self):  # is this useful test?
        self.grocerylist_app.start
        self.assertEqual(self.grocerylist_app.print_list(), None)

    def test_adding_a_product_and_quantity_is_on_the_list(self):
        self.grocerylist_service.empty_whole_list()
        self.grocerylist_service.add_product(
            self.grocery_item.product, self.grocery_item.quantity, self.grocery_item.store)
        products = self.grocerylist_service.get_products()
        self.assertEqual((products[0][0], products[0][1], products[0]
                         [2]), ("milk", 1, "K-market"))  # Korjaa tätä

    # added with quantities 29.11 & store 2.12
    def test_adding_products_and_quantities_are_on_the_list(self):
        self.grocerylist_service.empty_whole_list()
        self.grocerylist_service.add_product("milk", 2, "K-market")
        self.grocerylist_service.add_product("pineapple", 5, "Lidl")
        products = self.grocerylist_service.get_products()
        self.assertEqual(
            (products[0][0], products[1][1], products[1][2]), ("milk", 5, "Lidl"))

    def test_adding_a_product_already_on_the_list_not_success(self):
        self.grocerylist_service.empty_whole_list()
        self.grocerylist_service.add_product("milk", 2, "Lidl")
        self.assertRaises(ProductAlreadyOnListError,
                          lambda: self.grocerylist_service.add_product("milk", 2, "Lidl"))

    # added 26.11(vko4), updated with quantities 29.11(vko5) & store
    def test_deleting_a_product(self):
        self.grocerylist_service.empty_whole_list()
        self.grocerylist_service.add_product("milk", 4, "Lidl")
        self.grocerylist_service.add_product("pineapple", 6, "K-market")
        self.grocerylist_service.delete_product("milk", "Lidl")
        products = self.grocerylist_service.get_products()
        self.assertEqual(
            (products[0][0], products[0][1], products[0][2]), ("pineapple", 6, "K-market"))

    def test_delete_product_not_on_the_list_error(self):
        self.grocerylist_service.empty_whole_list()
        self.assertRaises(
            ProductNotOnListError, lambda: self.grocerylist_service.delete_product("milk", "Lidl"))

    # added 26.11, updated with quantities 29.11
    def test_empty_whole_list(self):
        self.grocerylist_service.empty_whole_list()
        self.grocerylist_service.add_product("milk", 7, "Lidl")
        self.grocerylist_service.add_product("pineapple", 6, "K-market")
        # self.grocerylist_service.delete_product("chocolate") #move to some other?
        self.grocerylist_service.empty_whole_list()
        products = self.grocerylist_service.get_products()
        self.assertEqual(len(products), 0)

    def test_get_products_per_store(self):
        self.grocerylist_service.empty_whole_list()
        self.grocerylist_service.add_product("milk", 7, "Lidl")
        self.grocerylist_service.add_product("choco", 3, "Lidl")
        self.grocerylist_service.add_product("beer", 6, "K-market")
        self.grocerylist_service.add_product("sausage", 6, "K-market")
        products1 = self.grocerylist_service.get_products_store("Lidl")
        products2 = self.grocerylist_service.get_products_store("K-market")
        self.assertEqual((products1[0][0], products1[1][0]), ("milk", "choco"))
        self.assertEqual(
            (products2[0][0], products2[1][0]), ("beer", "sausage"))
