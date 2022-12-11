
class Grocerylist:
    """Luokka, joka kuvaa kauppalistan riviä.

        Attributes:
            product: Merkkijono, joka kuvaa yksittäistä tuotetta
            quantity: Lukuarvo, joka kuvaa tuotteen määrää, voi olla myös tyhjä
                    tai sanallinen (esim. nippu)
            store: Merkkijono, joka kertoo lisätyn tuotteen kaupan
        """
    def __init__(self, product: str, quantity: int, store: str):
        """Luokan konstruktori, joka luo uuden kauppalista olion.

        Args:
            product: Merkkijono, joka kuvaa yksittäistä tuotetta
            quantity: Lukuarvo, joka kuvaa tuotteen määrää, voi olla myös tyhjä
                    tai sanallinen (esim. nippu)
            store: Merkkijono, joka kertoo lisätyn tuotteen kaupan
        """

        self.product = product
        self.quantity = quantity
        self.store = store
