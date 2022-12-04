
class Grocerylist:
    def __init__(self, product: str, quantity: int, store: str):
        #self.grocerylist = []
        self.product = product
        self.quantity = quantity
        self.store = store

    # def __str__(self):
        # tää piti olla että printaa tuotteet, eikä objektia 0x
        # return str(self.product)
        # return f"{str(self.product)} - {self.quantity}" #muut 28.11

    # def __eq__(self, other):
    #    return self.product == other.product
