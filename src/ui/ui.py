from services.grocerylist_service import GrocerylistService


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
        product = input("Anna tuote: ")
        #quantity = input ("Anna määrä: ")    #added . 28.11
        try:
            product = int(product)
            print("Annoit numeroita!")

        except ValueError:
            self._list.add_product(product) #, quantity) #muok. 28.11

    def remove(self):  # added 22.11
        self.print_list()
        remove_this = input("Anna poistettava tuote: ")
        self._list.delete_product(remove_this)

    def print_list(self):
        list_all = self._list.get_products()
        if list_all:
            for product in list_all:
                print(product)
            return
        else:
            print("Kauppalista on tyhjä.")
            return

    def empty_list(self):  # added 26.11
        check = input("Haluatko varmasti tyhjentää koko listan - kylla/ei?: ")
        if check == "kylla":
            self._list.empty_whole_list()
        else:
            return self.user_instructions()

    def start(self):
        self.user_instructions()
        while True:
            action = input("Valitse toiminto: ")
            if action == "0":
                break
            elif action == "1":
                self.add()
            elif action == "2":  # added 22.11
                self.remove()
            elif action == "3":
                self.print_list()
            elif action == "4":
                self.empty_list()
            else:
                self.user_instructions()
