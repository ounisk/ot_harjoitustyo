from entities.grocerylist_entity import Grocerylist
from repositories.grocerylist_repository import (
    grocerylist_repository as default_grocerylist_repository)


class ProductAlreadyOnListError(Exception):
    pass


class ProductNotOnListError(Exception):
    pass


class GrocerylistService:
    """Luokka, joka vastaa sovelluslogiikasta.
    Attributes:
        grocerylist_repository: GrocerylistRepository-olio, jolla on GrocerylistRepository
                                luokkaa vastaavat metodit käytössä.
    """

    def __init__(self, grocerylist_repository=default_grocerylist_repository):
        """Luokan konstruktori.

        Args:
            grocerylist_repository: GrocerylistRepository-olio, jolla on GrocerylistRepository
                                    luokkaa vastaavat metodit käytössä.
        """
        self._grocerylist_repository = grocerylist_repository

    def add_product(self, product: str, quantity: int, store: str):
        """Metodi, joka vastaa lisää tuotteen kauppalistalle sekä historia-arkistoon,
            tarkistaa ensin, että tuote ei ole jo ko.kaupan listalla.

        Args:
            product: merkkijono, tuotteen nimi
            quantity: lukuarvo, tuotteen määrä
            store: kaupan nimi, jonka listalle tuote lisätään

        Returns:
            Lisätty tuote Grocerylist-olion muodossa

        Raises:
            ProductAlreadyOnListError: virhe, joka tulee kun tuote on jo ko.kaupan listalla.

        """
        product_is_on_list = self._grocerylist_repository.find_product(
            product, store)

        if product_is_on_list:
            raise ProductAlreadyOnListError("Tuote on jo listalla!")

        product = Grocerylist(product=product, quantity=quantity, store=store)

        add = self._grocerylist_repository.add(product)
        add_to_history = self._grocerylist_repository.add_to_history(product)
        return add, add_to_history


    def delete_product(self, product, store):
        """Metodi, jolla tuote poistetaan kaupan listalta.

        Args:
            product: tuote, joka poistetaan
            store: kauppa, jonka listalta tuote poistetaan

        Raises:
            ProductNotOnListError: virhe, joka tulee, jos tuotteen poisto epäonnistuu, koska tuote
                                    ei ole ko.kaupan listalla.

        """
        try:
            self._grocerylist_repository.delete(product, store)
        except TypeError:
            raise ProductNotOnListError("Tuotetta ei ole listalla!")

    def modify_quantity(self, product, quantity, store):
        """Metodi, jolla voidaan muokata listalla olevan tuotteen määrää, ensin tarkistetaan,
            että tuote on ko.kaupan listalla.

        Args:
            product: tuote, jonka määrää muokataan
            quantity: tuotteen uusi määrä
            store: kauppa, jonka listalla tuote on

        Returns:
            Palauttaa tuotteen, jossa määrä muokattu.

        Raises:
            ProductNotOnListError: virhe, jos yritetään muokata määrää tuotteelle, joka
                                    ei ole ko.kaupan listalla.

        """
        product_is_on_list = self._grocerylist_repository.find_product(
            product, store)

        if not product_is_on_list:
            raise ProductNotOnListError("Tuotetta ei ole listalla!")

        return self._grocerylist_repository.modify_quantity_for_product(product, quantity, store)

    def empty_whole_list(self):
        """Metodi, jolla tyhjennetään molempien kauppojen ostoslistat.

        """
        self._grocerylist_repository.empty_all()

    def get_products(self):
        """Metodi, joka palauttaa listana molempien kauppojen kaikki tuotteet määrineen.

        Returns:
            Grocerylist-olioita sisältävä lista kaikista tuotteista määrineen.

        """
        return self._grocerylist_repository.list_products()

    def get_products_store(self, store):
        """Metodi, joka palauttaa kauppakohtaisen listan tuotteista määrineen.

        Args:
            store: kauppa, jonka tuotteet halutaan hakea.

        Returns:
            Grocerylist-olioita sisältävä kauppakohtainen lista tuotteista määrineen.
         """
        return self._grocerylist_repository.list_products_store(store)

    def get_top3_products(self):
        """Metodi, joka palauttaa listana kolme yleisimmin kauppalistalla esiintynyttä tuotetta.

        Returns:
            Grocerylist-olioita sisältävä lista kolmesta yleisimmistä tuotenimestä.
         """
        return self._grocerylist_repository.get_top3()


grocerylist_service = GrocerylistService()
