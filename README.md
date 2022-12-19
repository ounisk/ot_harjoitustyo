
# Ostoslista-sovellus

Sovelluksen tarkoituksena on toimia perheen sisäisenä kauppalistana ruokaostoksia varten. Sovellus on useamman käyttäjän käytettävissä, lisäksi se on toiminnoiltaan sujuva ja helppo käyttää.

Toimintoja ovat tuotteen ja mahdollisen määrän lisäys valittuun kauppaan, tuotteen poisto, tuotteen määrän muokkaus, TOP3-lista ja kaikkien listojen tyhjennys. Käyttöliittymä on tekstikäyttöliittymä. 

Sovelluksen toiminta on testattu Python 3.8 -versiolla. Käytettäessä muita versioita ongelmia saattaa esiintyä.

Sovellus on tehty Helsingin yliopiston Ohjelmistotekniikka-kurssin harjoitustyönä syksyllä 2022.

This is a course project for a software engineering course at the University of Helsinki. The software is a grocery list application suitable for family use.


## Dokumentaatio:

[Käyttöohje](https://github.com/ounisk/ot_harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)

[Vaatimusmäärittely](https://github.com/ounisk/ot_harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Arkkitehtuurikuvaus](https://github.com/ounisk/ot_harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

[Testausdokumentti](https://github.com/ounisk/ot_harjoitustyo/blob/master/dokumentaatio/testausdokumentti.md)

[Työaikakirjanpito](https://github.com/ounisk/ot_harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)

[Changelog](https://github.com/ounisk/ot_harjoitustyo/blob/master/dokumentaatio/changelog.md)




## Releases:
### Viimeisin versio:
[loppupalautus](https://github.com/ounisk/ot_harjoitustyo/releases/tag/loppupalautus)

### Aiemmat versiot:
[viikko 6 - release](https://github.com/ounisk/ot_harjoitustyo/releases/tag/viikko6)

[viikko 5 - release](https://github.com/ounisk/ot_harjoitustyo/releases/tag/viikko5)


## Asennus:
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

## Komentorivitoiminnot:
1. Ohjelman suorittaminen tapahtuu komennolla:
```
poetry run invoke start
```
2. Testit suoritetaan komennolla:
```
poetry run invoke test
```
3. Testikattavuus raportti luodaan ao. komennolla ja se generoituu *htmlcov*-hakemistoon tiedostoon *index.html*
```
poetry run invoke coverage-report
```
4. Tiedostossa *.pylintrc* määritellyt tarkistukset suoritetaan komennolla:
```
poetry run invoke lint
```
5. Koodin automaattinen formatointi autopep8-kirjastolla suoritetaan komennolla:
```
poetry run invoke format
```

