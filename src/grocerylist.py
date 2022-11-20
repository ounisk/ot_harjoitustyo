class Grocerylist:
    def __init__(self):
        self._groceries = []

    def add_product(self, product: str):
        if product in self._groceries:
            print("Tuote on jo listalla")
            return
        else:    
            self._groceries.append(product)
            #return    

    def get_products(self):
        if not self._groceries:
            return None
        else:
            return self._groceries

    # add modify and delete        
