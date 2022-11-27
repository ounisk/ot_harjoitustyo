import unittest
from services.grocerylist_service import GrocerylistService
# from grocerylist import Grocerylist    vanha
from ui.ui import Grocerylist_app


class TestGrocerylist_app(unittest.TestCase):
    def setUp(self):
        self.grocerylist_app = Grocerylist_app()
        self.grocerylist = GrocerylistService()

    def test_newly_created_list_is_empty(self):  # is this useful test?
        self.grocerylist_app.start
        self.assertEqual(self.grocerylist_app.print_list(), None)

    def test_adding_a_product_is_on_the_list(self):
        self.grocerylist.empty_whole_list()  # tyhjentää aluksi listan
        self.grocerylist.add_product("milk")
        products = self.grocerylist.get_products()
        self.assertEqual(products[0].product, "milk")

    def test_adding_products_are_on_the_list(self):
        self.grocerylist.empty_whole_list()  # tyhjentää aluksi listan
        self.grocerylist.add_product("milk")
        self.grocerylist.add_product("pineapple")
        products = self.grocerylist.get_products()
        self.assertEqual(products[0].product, "milk", "pineapple")

    def test_adding_a_product_already_on_the_list_not_success(self):
        self.grocerylist.empty_whole_list()  # tyhjentää aluksi listan
        self.grocerylist.add_product("milk")
        self.grocerylist.add_product("milk")
        self.assertEqual(len(self.grocerylist.get_products()), 1)

    def test_deleting_a_product(self):  # added 26.11
        self.grocerylist.empty_whole_list()  # tyhjentää aluksi listan
        self.grocerylist.add_product("milk")
        self.grocerylist.add_product("pineapple")
        self.grocerylist.delete_product("milk")
        products = self.grocerylist.get_products()
        self.assertEqual(products[0].product, "pineapple")

    def test_emptying_the_whole_list(self):  # added 26.11
        self.grocerylist.empty_whole_list()  # tyhjentää aluksi listan
        self.grocerylist.add_product("milk")
        self.grocerylist.add_product("pineapple")
        self.grocerylist.delete_product("chocolate")
        self.grocerylist.empty_whole_list()
        self.assertEqual(len(self.grocerylist.get_products()), 0)


# HUOM These are before changing to repository architecture

# class TestGrocerylist_app(unittest.TestCase):
#    def setUp(self):
#        self.grocerylist_app = Grocerylist_app()
#        self.grocerylist = Grocerylist()

#    def test_newly_created_list_is_empty(self):
#        self.grocerylist_app.start
        # self.assertEqual(self.grocerylist.get_products(), None) #alkup.
        #self.assertEqual(self.grocerylist_app.print_list(), None)
#        self.assertEqual(self.grocerylist.get_products(), None)  #uusi

#    def test_adding_a_product_is_on_the_list(self):
#        self.grocerylist.add_product("milk")
#        self.grocerylist.add_product("ananas")
        #self.assertEqual(self.grocerylist.get_products()[0], "milk")
#        self.assertEqual(self.grocerylist.get_products(), ['milk', 'ananas'])
        # self.assertEqual(self.grocerylist_app.print_list(), "milk") # tulee: None != "milk", miksi???

#    def test_adding_a_product_already_on_the_list_not_success(self):
#           self.grocerylist.add_product("milk")
#           self.grocerylist.add_product("milk")
#           self.assertEqual(len(self.grocerylist.get_products()), 1)

    # def lisää testi joka testaa tuotteen poistoa
