from grocerylist import Grocerylist

class Grocerylist_app:
    def __init__(self):
        self._list = Grocerylist()

    def user_instructions(self):
        print("Toiminnot:")
        print("0 - lopeta")
        print("1 - lisää tuote")
        print("2 - poista tuote")  
        print("3 - tulosta lista")  

    def add(self):
        product = input("Anna tuote: ")
        self._list.add_product(product)

    #def remove(self):
        #printlist and select product to be removed
        #product = input
    
    def print_list(self):
        list_all = self._list.get_products()
        if list_all:
            for product in list_all:
                print(product)
            return    
        else:
            print ("Kauppalista on tyhjä.")
            return
        

    def start(self):
        self.user_instructions()
        while True:
            action = input("Valitse toiminto: ")
            if action == "0":
                break
            elif action == "1":
                self.add()
            #elif action == "2":  #add this
            #    self.remove()        
            elif action == "3":
                self.print_list()       
            else:
                self.user_instructions()