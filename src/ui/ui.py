from services.grocerylist_service import GrocerylistService, ProductAlreadyOnListError, ProductNotOnListError
from termcolor import cprint


class Grocerylist_app:
    def __init__(self):
        self._list = GrocerylistService()

    def user_instructions(self):
        print("Toiminnot:")
        print("0 - lopeta")
        print("1 - lisää tuote")
        print("2 - poista tuote")
        print("3 - muokkaa tuotteen määrää")
        print("4 - tulosta lista")
        print("5 - näytä tuotteiden top3")
        print("6 - tyhjennä koko lista")

    def add(self):
        store = input("Lisää tuote kauppaan - K-market vai Lidl?: ")
        if store not in ["K-market", "Lidl"]:
            print("Kauppa ei valittavissa!")
            return
        product = input("Anna tuote: ")
        if not (product.strip()):
            print("Annoit tyhjän tuotekentän!")
            return
        quantity = input("Anna määrä, jos haluat: ")
        try:
            product = int(product)
            print("Annoit numeroita!")

        except ValueError:
            try:
                self._list.add_product(product, quantity, store)
            except ProductAlreadyOnListError:
                print("Tuote on jo listalla!")

    def remove(self):
        self.print_list()
        remove_from = input("Poista kaupan listalta - K-market vai Lidl?: ")
        remove_this = input("Anna poistettava tuote: ")

        try:
            remove_this = int(remove_this)
            print("Annoit numeroita!")

        except ValueError:
            try:
                self._list.delete_product(remove_this, remove_from)
            except ProductNotOnListError:
                print("Tuotetta ei ole listalla!")

    def modify_product_quantity(self):
        self.print_list()
        modify_from = input("Muokkaa määrää listalla - K-market vai Lidl?: ")
        if modify_from not in ["K-market", "Lidl"]:
            print("Kauppaa ei ole!")
            return
        modify_product = input("Anna tuote, jonka määrää haluat muokata: ")
        if not (modify_product.strip()):
            print("Annoit tyhjän tuotekentän!")
            return

        new_quantity = input("Anna uusi määrä: ")
        try:
            self._list.modify_quantity(
                modify_product, new_quantity, modify_from)
        except ProductNotOnListError:
            print("Tuotetta ei ole listalla!")

    def print_list(self):
        list_all = self._list.get_products()

        if list_all:
            cprint("K-MARKET:", "green")
            list_store1 = self._list.get_products_store("K-market")
            if list_store1:
                for product in list_store1:
                    print(product[0], product[1])
            else:
                print("Kauppalista on tyhjä.")

            cprint("LIDL:", "green")
            list_store2 = self._list.get_products_store("Lidl")
            if list_store2:
                for product in list_store2:
                    print(product[0], product[1])
            else:
                print("Kauppalista on tyhjä.")

        else:
            cprint("K-MARKET:", "green")
            print("Kauppalista on tyhjä.")
            cprint("LIDL:", "green")
            print("Kauppalista on tyhjä.")
            return

    def empty_list(self):
        check = input("Haluatko varmasti tyhjentää koko listan - kylla/ei?: ")
        if check == "kylla":
            self._list.empty_whole_list()
        else:
            return self.user_instructions()

    def get_top3(self):
        list_top3 = self._list.get_top3_products()
        if list_top3:
            cprint("TOP3 tuotteet:", "green")
            for product in list_top3:
                print(product[0])
        else:
            print("TOP3 on tyhjä.")

    def start(self):
        cprint("***OSTOSLISTA***", "yellow", attrs=["bold"])
        self.user_instructions()
        while True:
            action = input("Valitse toiminto: ")
            if action == "0":
                break
            elif action == "1":
                self.add()
            elif action == "2":
                self.remove()
            elif action == "3":
                self.modify_product_quantity()
            elif action == "4":
                self.print_list()
            elif action == "5":
                self.get_top3()
            elif action == "6":
                self.empty_list()
            else:
                self.user_instructions()
