from services.grocerylist_service import GrocerylistService, ProductAlreadyOnListError, ProductNotOnListError


class Grocerylist_app:
    def __init__(self):
        self._list = GrocerylistService()

    def user_instructions(self):
        print("Toiminnot:")
        print("0 - lopeta")
        print("1 - lisää tuote")
        print("2 - poista tuote")
        print("3 - tulosta lista")
        print("4 - tyhjennä koko lista")

    def add(self):
        store = input("Lisää tuote kauppaan - K-market vai Lidl?: ")
        if store not in ["K-market", "Lidl"]:  # lisäys 2.12
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
            except ProductAlreadyOnListError:  # 4.12
                print("Tuote on jo listalla!")

    def remove(self):  # added 22.11
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

    def print_list(self):
        list_all = self._list.get_products()

        if list_all:
            print("K-MARKET:")
            list_store1 = self._list.get_products_store("K-market")
            if list_store1:
                for product in list_store1:
                    print(product[0], product[1])
                    #print (f"{product[0]:10}  {product[1]:10}")
            else:
                print("Kauppalista on tyhjä.")

            print("LIDL:")
            list_store2 = self._list.get_products_store("Lidl")
            if list_store2:
                for product in list_store2:
                    print(product[0], product[1])
                    #print (f"{product[0]:10}  {product[1]:10}")
            else:
                print("Kauppalista on tyhjä.")

        else:
            print("K-MARKET:")
            print("Kauppalista on tyhjä.")
            print("LIDL:")
            print("Kauppalista on tyhjä.")
            return

    def empty_list(self):  # added 26.11
        check = input("Haluatko varmasti tyhjentää koko listan - kylla/ei?: ")
        if check == "kylla":
            self._list.empty_whole_list()
        else:
            return self.user_instructions()

    def start(self):
        print("***OSTOSLISTA***")
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
                self.print_list()
            elif action == "4":
                self.empty_list()
            else:
                self.user_instructions()
