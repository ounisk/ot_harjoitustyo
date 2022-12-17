# Testausdokumentti

Ohjelman testaus on suoritettu automaattisilla yksikkö- ja integraatiotesteillä (unittest). Lisäksi on suoritettu manuaalista järjestelmätason testausta.


## Yksikkö- ja integraatiotestaus
### Sovelluslogiikka

Ohjelman sovelluslogiikasta vastaa *Services*-pakkauksen ```GrocerylistService```-luokka. Tätä luokaa testataan [TestGrocerylistService](https://github.com/ounisk/ot_harjoitustyo/blob/master/src/tests/grocerylist_services_test.py)-testiluokalla.
Testtauksessa riippuvuuksiksi on injektoitu repositorio-luokan olioita (*Grocerylist*-olio).
Sovellus käyttää tietokantaa ja testauksessa tämä on huomioitu käyttämällä testitietokantaa, jonka nimi on konfiguroitu *.env.test.*-tiedostossa.
Testauksen yhteydessä tietokanta alustetaan.

### Repositorio-luokka
*Repositories*- pakkauksen ```GrocerylistRepository```-luokkaa on testattu [TestGrocerylistRepository](https://github.com/ounisk/ot_harjoitustyo/blob/master/src/tests/grocerylist_repository_test.py)-testiluokalla. Testauksessa käytetään testitietokantaa, jonka 
nimi on konfiguroitu *.env.test.*-tiedostossa. Testauksen yhteydessä tietokanta alustetaan, kuten edellä Sovelluslogiikka-kohdassa.

### Testauskattavuus

(kuva tänne, huomioita mitä olisi voinut jättää ulkopuolelle)



## Järjestelmätestaus

Ohjelman järjestelmätestaus on suoritettu manuaalisesti. Testausta on suoritettu Linux-ympäristössä sekä yliopiston virtuaaliympäristössä.



