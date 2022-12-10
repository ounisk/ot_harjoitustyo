# Käyttöohje:
Projektin viimeisimmän version löydät [Releases-osiosta](https://github.com/ounisk/ot_harjoitustyo/releases), jossa valitaan on Assets-otsikon alta *Source code*.

## Konfigurointi:
Sovellus lukee ja tallentaa tietoja tietokantaan. Tietokantatiedoston nimi löytyy tiedostosta *.env*, jossa sitä voi
halutessaan muuttaa. Tietokantatiedoston default nimi on database_grocerylist.sqlite. Tiedostot luodaan hakemistoon *data*.

## Ohjelman asennus ja käynnistäminen:
1. Asenna ensin riippuvuudet komennolla:
```
poetry install
```
2. Alusta tietokanta komennolla:
```
poetry run invoke build
```
3. Käynnistä sovellus komennolla:
```
poetry run invoke start
```
## Ostoslista-sovelluksen käyttö:
Alkutoimenpiteiden jälkeen ohjelma avautuu tekstikäyttöliittymänä. Näkyvillä ovat sovelluksen toiminnot:

![image](https://user-images.githubusercontent.com/78747844/206838492-c7619351-180e-453c-81e3-45684a0a5520.png)

### Tuotteen lisääminen:
Käyttäjän halutessa lisätä tuotteen listalle, valitaan "1" ja seurataan näytön ohjeita. 

![image](https://user-images.githubusercontent.com/78747844/206839136-d59b2a40-bcca-4689-bb1e-d87a40ab3af9.png)

### Listalla olevan tuotteen poistaminen:
Jos käyttäjä haluaa poistaa listalla olevan tuotteen, valitaan "2". Sovellus näyttää ensin mitä tuotteita on listoilla ja pyytää sen jäkeen poistettava tuotteen.

![image](https://user-images.githubusercontent.com/78747844/206840671-b12b3cdd-0267-4619-a5e9-028e6f216732.png)


### Listalla olevan tuotteen määrän muuttaminen:
Mikäli käyttäjä haluaa muokata listalla olevan tuotteen määrää, valitaan "3". Käyttäjältä tiedustellaan kumman kaupan listalla olevan tuoteen määrää
muokataan (sama tuote voi olla molempien kauppojen listalla), tuoteen nimeä ja uutta määrää: 

![image](https://user-images.githubusercontent.com/78747844/206839805-bdb9858b-e885-4473-92cb-1b96103bc883.png)


### Listojen tulostaminen näytölle:
Kun käyttäjä haluaa tarkastaa mitä tuotteita ostolistaan on lisätty, valitaan "4". Tällöin nähdään, mitä tuotteita on kauppojen listoilla.

![image](https://user-images.githubusercontent.com/78747844/206840425-ce8ed3b4-7630-445d-8e33-debcdf2c9187.png)


### TOP3-tuotteet:
Jos käyttäjä haluaa tarkastella koko ostoslistan käyttöhistorian yleisimpiä tuotteita, niin valitsemalla "5" nähdään TOP3-lista:

![image](https://user-images.githubusercontent.com/78747844/206840017-726e4136-3e41-4330-a2ae-0c8c584db77c.png)

### Ostoslistojen tyhjentäminen:
Mikäli käyttäjä haluaa tyhjentää koko ostoslistan (molempien kauppojen listat) valitaan "6". Käyttäjältä varmistetaan vielä, että hän haluaa tyhjentää koko listan.

![image](https://user-images.githubusercontent.com/78747844/206840209-5b8dcb52-7917-4819-bb81-c07dd2c5b91c.png)

### Ostoslista-sovelluksen lopettaminen:
Käyttäjä valitsee "0", jolloin sovellus sulkeutuu.


