import unittest
from entities.grocerylist_entity import Grocerylist
from repositories.grocerylist_repository import grocerylist_repository


class TestGrocerylistRepository(unittest.TestCase):
    def setUp(self):
        grocerylist_repository.empty_all()
        self.grocerylist_kmarket = Grocerylist("bread", 1, "K-market")
        self.grocerylist_lidl = Grocerylist("coffee", 100, "Lidl")

    def test_list_products(self):
        grocerylist_repository.add(self.grocerylist_kmarket)
        grocerylist_repository.add(self.grocerylist_lidl)
        products = grocerylist_repository.list_products()
        self.assertEqual(len(products), 2)
        self.assertEqual(products[1][2], "Lidl")

    def test_list_products_store(self):
        grocerylist_repository.add(self.grocerylist_kmarket)
        grocerylist_repository.add(self.grocerylist_lidl)
        products = grocerylist_repository.list_products_store("K-market")
        self.assertEqual((products[0][0], products[0][1]), ("bread", 1))

    def test_find_product(self):
        grocerylist_repository.add(self.grocerylist_kmarket)
        grocerylist_repository.add(self.grocerylist_lidl)
        products = grocerylist_repository.find_product("coffee", "Lidl")
        self.assertEqual(products[0][0], "coffee")

    def test_add(self):
        grocerylist_repository.add(self.grocerylist_kmarket)
        grocerylist_repository.add(self.grocerylist_lidl)
        products = grocerylist_repository.list_products()
        self.assertEqual(len(products), 2)
        self.assertEqual((products[0][1], products[1][0]), (1, "coffee"))

    def test_delete(self):
        grocerylist_repository.add(Grocerylist("coffee", 1, "K-market"))
        grocerylist_repository.add(self.grocerylist_lidl)
        grocerylist_repository.delete("coffee", "Lidl")
        products = grocerylist_repository.list_products()
        self.assertEqual(len(products), 1)
        self.assertEqual(
            (products[0][0], products[0][2]), ("coffee", "K-market"))

    def test_modify_quantity_for_product(self):
        grocerylist_repository.add(self.grocerylist_kmarket)
        grocerylist_repository.modify_quantity_for_product(
            "bread", 123, "K-market")
        products = grocerylist_repository.list_products()
        self.assertEqual(products[0][1], 123)

    def test_empty_all(self):
        grocerylist_repository.add(self.grocerylist_kmarket)
        grocerylist_repository.add(self.grocerylist_lidl)
        grocerylist_repository.empty_all()
        products = grocerylist_repository.list_products()
        self.assertEqual(len(products), 0)

    def test_get_top3(self):
        grocerylist_repository.empty_history()
        grocerylist_repository.add_to_history(self.grocerylist_kmarket)
        top3 = grocerylist_repository.get_top3()
        self.assertEqual(top3[0][0], "bread")
        
