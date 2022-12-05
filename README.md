
# Ostoslista-sovellus

Sovelluksen tarkoituksena on toimia perheen sisäisenä kauppalistana ruokaostoksia varten. Sovellus on useamman käyttäjän käytettävissä, lisäksi se on toiminnoiltaan sujuva ja helppo käyttää.

Toimintoja ovat tuotteen ja mahd. määrän lisäys valittuun kauppaan, tuotteen poisto ja kaikkien listojen tyhjennys. Käyttöliittymä on tekstikäyttöliittymä. 

Sovellus on tehty Helsingin yliopiston Ohjelmistotekniikka-kurssin harjoitustyönä syksyllä 2022.

This is a course project for a software engineering course at the University of Helsinki. The software is a grocery list application suitable for family use.


### Dokumentaatio:
[vaatimusmaarittely.md](https://github.com/ounisk/ot_harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[tyoaikakirjanpito.md](https://github.com/ounisk/ot_harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)

[changelog.md](https://github.com/ounisk/ot_harjoitustyo/blob/master/dokumentaatio/changelog.md)

[arkkitehtuuri.md](https://github.com/ounisk/ot_harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)


### Release:
[viikko 5 - release](https://github.com/ounisk/ot_harjoitustyo/releases/tag/viikko5)


### Asennus:
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

### Komentorivitoiminnot:
Ohjelman suorittaminen tapahtuu komennolla:
```
poetry run invoke start
```
Testit suoritetaan komennolla:
```
poetry run invoke test
```
Testikattavuus raportti luodaan ao. komennolla ja se generoituu *htmlcov*-hakemistoon tiedostoon *index.html*
```
poetry run invoke coverage-report
```
Tiedostossa *.pylintrc* määritellyt tarkistukset suoritetaan komennolla:
```
poetry run invoke lint
```
