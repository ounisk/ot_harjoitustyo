
class Grocerylist:  # list for one store
    def __init__(self, product: str):  # , quantity):  #lisää store_id???
        self.grocerylist = []
        self.product = product

        #self.quantity= quantity

    def __str__(self):
        # tää piti olla etttä printaa tuotteet, eikä objektia 0x
        return str(self.product)

    # def __eq__(self, other):
    #    return self.product == other.product
