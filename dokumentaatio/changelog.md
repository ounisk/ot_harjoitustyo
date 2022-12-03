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
- Lisätty testi koskien kauppakohtaisia listoja (tuotteiden ja määrien oikeellisuus) sekä testi koskien listalla olemattoman tuotteen poistoyritystä
