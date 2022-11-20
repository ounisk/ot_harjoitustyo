import unittest
from grocerylist import Grocerylist
from ui.ui import Grocerylist_app 

class TestGrocerylist_app(unittest.TestCase):
    def setUp(self):
        self.grocerylist_app = Grocerylist_app()
        self.grocerylist = Grocerylist()

    def test_newly_created_list_is_empty(self):
        self.grocerylist_app.start
        #self.assertEqual(self.grocerylist.get_products(), None) #alkup.
        #self.assertEqual(self.grocerylist_app.print_list(), None)
        self.assertEqual(self.grocerylist.get_products(), None)  #uusi

    def test_adding_a_product_is_on_the_list(self):
        self.grocerylist.add_product("milk")
        self.grocerylist.add_product("ananas")
        #self.assertEqual(self.grocerylist.get_products()[0], "milk")
        self.assertEqual(self.grocerylist.get_products(), ['milk', 'ananas'])
        ##self.assertEqual(self.grocerylist_app.print_list(), "milk") # tulee: None != "milk", miksi???


    def test_adding_a_product_already_on_the_list_not_success(self):
           self.grocerylist.add_product("milk")
           self.grocerylist.add_product("milk")
           self.assertEqual(len(self.grocerylist.get_products()), 1)