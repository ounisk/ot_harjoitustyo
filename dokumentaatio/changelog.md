## Viikko 3
- Projektin rakenteen ja toimintojen luonti
- Luotu käyttöliitymä - alustavasti tekstipohjainen ja suppeilla toiminnoilla
- Luotu alustavaa toiminnallisuutta, mm. tavaroiden lisääminen kauppalistaan ja kauppalistan tuotteiden listaaminen
- Ensimmäiset toimintoja koskevat testit

## Viikko 4
- Muutettu projektin rakenne ja arkkitehtuuri vastaamaan *repository*-sunnittelumallia ja implementoitu tämän vaatimat muutokset hakemistoihin ja tiedostoihin
- Muutettu aiempi tallennusmuoto (tietorakenteena oli ensin pelkkä lista), siten että tieto tallennetaan ja luetaan .csv-tiedostosta
- Lisätty toiminnallisuuksiin tavaroiden poisto ja koko listan tyhjentäminen
- Lisätty testeihin uusia toiminnallisuuksia (poisto ja koko listan tyhjentäminen) koskevat testit

## Viikko 5
- Lisätty toiminnallisuus, joka mahdollistaa määrien syöttämisen
- Lisätty toiminnallisuus, joka mahdollistaa tuotteiden syöttämisen haluttuun kauppaan ja tuotteiden poiston halutun kaupan listalta
- Siirrytty aiemmasta tallennusmuodosta (.csv-tiedosto) SQLite-tietokantaan ja tehty sen vaatimat muutokset hakemistoihin ja tiedostoihin
- Lisätty testi koskien kauppakohtaisia listoja (tuotteiden ja määrien oikeellisuus), testi koskien virhetilanteita: listalla olemattoman tuotteen poistoyritys sekä listalla jo olevan tuotteen lisäämisyritys 

## Viikko 6
- Luotu tietokantaoperaatioiden testaukseen oma tiedosto ja sitä koskevat testit, ts. eriytetty services-testit ja repository-testit
- Lisätty "määrän muokkaus" -toiminnallisuus
- Lisätty TOP3-toiminnallisuus, joka listaa kolme yleisintä ostoslistan tuotetta
- Lisätty riippuvuudeksi ulkoinen termcolor-kirjasto, jolla toteutettu värejä tekstikäyttöliittymään
- Lisätty testejä uusille toiminnallisuuksille (määrän muokkaus, TOP3) ja refaktoroitu vanhaa koodia
