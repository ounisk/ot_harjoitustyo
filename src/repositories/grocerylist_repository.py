from entities.grocerylist_entity import Grocerylist
from database_connection import get_database_connection


class GrocerylistRepository:
    """Luokka, joka vastaa kauppalistaan kohdistuvista tietokantaoperaatioista.

    """

    def __init__(self, connection):
        """ Luokan konstruktori.

        Args:
            connection (connection -olio): tietokantayhteyden olio
        """
        self._connection = connection

    def list_products(self):
        """ Hakee tietokannasta kaikki tiedot: tuote, määrä, kauppa.

        Returns:
            Palauttaa listan kauppalista-olioita, mikäli niitä on.
            Muutoin palauttaa None
        """

        cursor = self._connection.cursor()

        cursor.execute(
            "SELECT product, quantity, store FROM Groceries ORDER BY store")
        rows = cursor.fetchall()

        products = []

        for row in rows:
            products.append(row)
        return products

    def list_products_store(self, in_store):
        """Hakee tietokannasta kauppakohtaiset tiedot.

        Args:
            in_store: kauppa, jonka tiedot haetaan.

        Returns:
            Palauttaa listana kauppakohtaiset tuotteet määrineen.
            Jos niitä ei ole, niin palauttaa None.
        """

        cursor = self._connection.cursor()
        cursor.execute(
            """SELECT product, quantity FROM Groceries WHERE store =(?)""", [in_store])
        rows = cursor.fetchall()

        if rows:
            products = []

            for row in rows:
                products.append(row)
            return products

    def find_product(self, find_product, in_store):
        """Etsii onko tietyn kaupan listalla tietty tuote.

        Args:
            find_product: tuote, jota etsitään.
            in_store: kauppa, josta tuotetta etsitään.

        Returns:
            Palauttaa tuotteen, jos se on kaupan listalla.
            Jos tuote ei ole kaupan listalla, palauttaa None.
        """

        cursor = self._connection.cursor()
        cursor.execute("SELECT product FROM Groceries WHERE product = (?) AND store =(?)",
                       [find_product, in_store])
        rows = cursor.fetchall()

        products = []

        for row in rows:
            products.append(row)
        return products

    def add(self, new_product: Grocerylist):
        """Lisää Grocerylist-olion tietokantaan.

        Args:
            new_product: Grocerylist-olio, joka lisätään tietokantaan.
        """

        cursor = self._connection.cursor()
        cursor.execute("INSERT INTO Groceries (product, quantity, store) VALUES (?,?, ?)",
                       [new_product.product, new_product.quantity, new_product.store])
        self._connection.commit()

    def delete(self, product_delete, from_store):
        """Poistaa halutun tuotteen halutusta kaupasta.

        Args:
            product_delete: tuote, joka halutaan poistaa.
            from_store: kauppa, jonka listalta tuote halutaan poistaa.

        """
        cursor = self._connection.cursor()
        cursor.execute("SELECT id FROM Groceries WHERE product = (?) AND store =(?)",
                       [product_delete, from_store])

        del_id = cursor.fetchone()[0]
        cursor.execute("DELETE FROM Groceries WHERE id = (?)", [del_id])
        self._connection.commit()

    def modify_quantity_for_product(self, product_modify, new_quantity, from_store):
        """Metodi, joka muokkaa halutun tuotteen määrää tietyn kaupan listalla.

        Args:
            product_modify: tuote, jonka määrää halutaan muokata.
            new_quantity: tuotteen uusi määrä.
            from_store: kauppa, jonka listalla tuote on.

        """
        cursor = self._connection.cursor()
        cursor.execute("UPDATE Groceries SET quantity = (?) WHERE product = (?) AND store = (?)", [
                       new_quantity, product_modify, from_store])
        self._connection.commit()

    def empty_all(self):
        """Metodi, joka tyhjentää tietokannan kaikista tiedoista eli tyhjentää kauppalistat.

        """

        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM Groceries")
        self._connection.commit()

    def empty_history(self):
        """Metodi, joka tyhjentää kaikkien kauppalistojen koko tuotehistorian.
            Tätä metodia käytetään vain testausksessa.
        """

        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM History")
        self._connection.commit()

    def add_to_history(self, new_product: Grocerylist):
        """Metodi, joka lisää Grocerylist-olion historiatiedot kattavaan tietokantaan.

        Args:
            new_product: Grocerylist-olio, joka lisätään tietokantaan.

        """
        cursor = self._connection.cursor()
        cursor.execute("INSERT INTO History (product, store) VALUES (?,?)", [
                       new_product.product, new_product.store])
        self._connection.commit()

    def get_top3(self):
        """Metodi, joka hakee History-tietokannasta kolme
            yleisintä tuotetta sovelluksen historiassa.

        Returns:
            Paluttaa listan kolmesta yleisimmästä tuotteesta.
            Jos sovellus on juuri otettu käyttöön eikä tuotteita ole lisätty kauppalistoille
            niin, palauttaa None.

        """

        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT product FROM History GROUP BY product ORDER BY COUNT(*) DESC LIMIT 3")
        rows = cursor.fetchall()

        products = []

        for row in rows:
            products.append(row)
        return products


grocerylist_repository = GrocerylistRepository(get_database_connection())
