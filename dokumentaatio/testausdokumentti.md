# Testausdokumentti

Ohjelman testaus on suoritettu automaattisilla yksikkö- ja integraatiotesteillä (unittest). Lisäksi on suoritettu manuaalista järjestelmätason testausta.


## Yksikkö- ja integraatiotestaus
### Sovelluslogiikka

Ohjelman sovelluslogiikasta vastaa *Services*-pakkauksen ```GrocerylistService```-luokka. Tätä luokaa testataan [TestGrocerylistService](https://github.com/ounisk/ot_harjoitustyo/blob/master/src/tests/grocerylist_services_test.py)-testiluokalla.
Testauksessa riippuvuuksiksi on injektoitu repositorio-luokan olioita (*Grocerylist*-olio).
Sovellus käyttää tietokantaa ja testauksessa tämä on huomioitu käyttämällä testitietokantaa, jonka nimi on konfiguroitu *.env.test.*-tiedostossa.


### Repositorio-luokka
*Repositories*- pakkauksen ```GrocerylistRepository```-luokkaa on testattu [TestGrocerylistRepository](https://github.com/ounisk/ot_harjoitustyo/blob/master/src/tests/grocerylist_repository_test.py)-testiluokalla. Testauksessa käytetään testitietokantaa, jonka 
nimi on konfiguroitu *.env.test.*-tiedostossa.

### Testauskattavuus

Testauksen haarautumakattavuus ilman *UI*-pakkausta (käyttöliittymä) on 93%. Testauksen ulkopuolelle jätettiin myös *index.py*-tiedosto.

![image](https://user-images.githubusercontent.com/78747844/208295427-ace4b008-a72a-4417-acbd-12241f48db37.png)

*Build.py*-tiedoston suoritusta komentoriviltä ei testattu, tiedoston olisi voinut jättää testikattavuuden ulkopuolelle. 


## Järjestelmätestaus

Ohjelman järjestelmätestaus on suoritettu manuaalisesti. Testausta on suoritettu Linux- sekä macOS-ympäristössä ja lisäksi yliopiston virtuaaliympäristössä.

## Ohjelman asennus ja konfigurointi
Ohjelma on asennettu seuraamalla [käyttöohjetta](https://github.com/ounisk/ot_harjoitustyo/blob/master/dokumentaatio/kayttoohje.md). Asennusta on testattu sekä kloonaamalla Git-projekti kohdekoneelle että lataamalla haluttu versio [Releases-](https://github.com/ounisk/ot_harjoitustyo/releases)osiosta.

Ohjelman käyttöä on testattu  ns. jatkuvassa käytössä, jossa ostoslistat ovat olleet jo olemassa ja tietokantatauluissa sekä myös tilanteissa alkaen asennuksesta, joissa mitään tietoja ei ole ollut.

## Toiminnallisuudet
Järjestelmätestauksessa on käyty läpi kaikki ohjelman tarjoamat toiminnallisuudet (ks. [vaatimusmäärittely](https://github.com/ounisk/ot_harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md) ja [käyttöohje](https://github.com/ounisk/ot_harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)). Lisäksi on testattu mahdollisia virhetilanteita, kuten mm. syöttäminen olemattomaan kauppaan, tyhjien kenttien antaminen sopimattomissa kohdissa, olemattomien tuotteiden poistoyritykset.  

## Sovellukseen jääneet laatuongelmat
- Mikäli käyttäjä ei seuraa käyttöohjeen ohjeistusta tietokannan alustamisen osalta (eli ei suorita komentoa ```poetry run invoke build```), niin virheilmoitus ei ole käyttäjäystävällinen.






