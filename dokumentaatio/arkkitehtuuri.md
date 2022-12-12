# Arkkitehtuurikuvaus

## Rakenne:
Koodin rakenne on kolmen tason kerrosarkkitehtuuri. Rakenteessa *ui* vastaa käyttöliittymästä, *services* vastaa sovelluslogiikasta ja *repositories* vastaa tietojen tallennuksesta. *entities* sisältää luokan, jonka perusteella sovelluksen käyttämät oliot on muodostettu. Pakkausrakennetta voidaan havainnollistaa seuraavasti:

![image](https://user-images.githubusercontent.com/78747844/206843117-edf13d7d-cbcd-4368-a443-c858d40ba2aa.png)

## Käyttöliittymä:
Sovelluksen käyttöliittymä on tekstikäyttöliittymä. Käyttöliittymä on eristetty sovelluslogiikasta - kaikki tulostaminen ja käyttäjän kanssa kommunikointi tapahtuu ainoastaan käyttöliittymässä (*ui*). Käyttöliittymästä kutsutaan sovelluslogiikan, eli GrocerylistService-luokan, metodeja.

## Sovelluslogiikka:
Sovelluksen tietorakenne pohjautuu luokan [Grocerylist](https://github.com/ounisk/ot_harjoitustyo/blob/master/src/entities/grocerylist_entity.py) käyttöön. Se muodostaa olion, joka kuvastaa yksittäistä ostoslistan riviä, jonka attribuutteja ovat tuote, määrä ja kauppa. Sovelluslogiikka sekä tietojen tallennus, luku ja haku hyödyntävät Grocerylist-luokkaa.

```mermaid
classDiagram
  class Grocerylist{
  +str product
  +int quantity
  +str store
  }
  ```
Sovelluksen toiminnallisuuksista ja sovelluslogiikasta vastaa [GrocerylistService-luokka](https://github.com/ounisk/ot_harjoitustyo/blob/master/src/services/grocerylist_service.py) ja sen ainoa olio. GrocerylistService-luokka tarjoaa metodit, joilla käyttöliittymän toiminnallisuudet toteutetaan. GrocerylistService-luokan metodeja ovat:

- `add_product(product, quantity, store)`

- `delete_product(product, store)`

- `modify_quantity(product, quantity, store)`

- `empty_whole_list()`

- `get_products()`

-  `get_products_store()`

-  `get_top3_products()`


Lisäksi GrocerylistService-luokalla on pääsy ostolistan tietojen tallennuksesta, lukemista ja hausta vastaavan [GrocerylistRepository-luokan](https://github.com/ounisk/ot_harjoitustyo/blob/master/src/repositories/grocerylist_repository.py) (pakkausrakenteessa *repositories*) metodeihin, mikä on mahdollistettu injektoimalla GrocerylistRepository-luokka GrocerylistService-luokkaan.     

Ohjelman rakennetta ja luokkien (GrocerylistService, GrocerylistRepository sekä Grocerylist) välisiä suhteita havainnollistetaan alla olevalla luokka-/pakkauskaaviolla:

![image](https://user-images.githubusercontent.com/78747844/206849601-bb0da61a-e4b1-4b31-a00e-e33fc79102e7.png)

## Tietojen pysyväistallennus:
Tietojen tallennuksesta, lukemista ja hausta vastaa [GrocerylistRepository-luokka](https://github.com/ounisk/ot_harjoitustyo/blob/master/src/repositories/grocerylist_repository.py) (pakkausrakenteessa *repositories*). Tiedot tallennetaan SQLite-tietokantaan.

### Tiedostot:
Tietokantatiedoston nimi on määritelty *.env*-tiedostossa. 
Grocerylist-oliot tallennetaan tietokantatauluihin *Groceries* ja *History*.

## Sekvenssikaavio
### Tuotteen lisääminen
  
```mermaid
sequenceDiagram
  actor User
  participant UI
  participant GrocerylistService
  participant GrocerylistRepository
  participant maito
  User ->> UI: selects "lisää tuote"
  UI ->> GrocerylistService: add_product("maito", 2, "K-market")
  GrocerylistService ->> GrocerylistRepository  : find_product("maito","K-market")
  GrocerylistRepository -->> GrocerylistService: None
  GrocerylistService ->> maito: Grocerylist("maito", 2, "K-market")
  GrocerylistService ->> GrocerylistRepository: add(Grocerylist("maito", 2, "K-market"))
  GrocerylistService ->> GrocerylistRepository: add_to_history(Grocerylist("maito", 2, "K-market"))
  GrocerylistRepository -->> GrocerylistService: product
  GrocerylistService -->> UI: product  
``` 
Toiminnallisuus alkaa käyttöliittymmässä, kun käyttäjä valitsee "lisää tuote" vaihtoehdon. Tämän jälkeen käyttäjä syöttää kaupan, tuotteen ja mahdollisen määrän. Käyttöliittymä kutsuu tämän jälkeen sovelluslogiikan *add_product* -metodia ja välittää annetut tiedot. Seuraavaksi sovelluslogiikka tarkastaa  *find_product* -metodilla onko ko.tuote jo ko.kaupan listassa. Mikäli näin ei ole (kuten tässä), niin sovelluslogiikka kutsuu seuraavaksi metodia *add(Grocerylist("maito", 2, "K-market"))* sekä *add_to_history(Grocerylist("maito", 2, "K-market"))*, jotka lisäävät *Grocerylist("maito", 2, "K-market")*-olion tietokannan tauluihin. Tämä jälkeen kontrolli palaa takaisin käyttöliittymään.

### Tuotteen poisto

### Määrän muokkaus

### Tuotteiden listaus

### Top3-tuotteiden listaus
