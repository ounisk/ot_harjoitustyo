# Arkkitehtuurikuvaus

## Rakenne:
Koodin rakenne on kolmen tason kerrosarkkitehtuuri. Rakenteessa *ui* vastaa käyttöliittymästä, *services* vastaa sovelluslogiikasta ja *repositories* vastaa tietojen tallennuksesta. *entities* sisältää luokan, jonka perusteella sovelluksen käyttämät oliot on muodostettu. Pakkausrakennetta voidaan havainnollistaa seuraavasti:

![image](https://user-images.githubusercontent.com/78747844/206843117-edf13d7d-cbcd-4368-a443-c858d40ba2aa.png)

## Käyttöliittymä:
Sovelluksen käyttöliittymä on tekstikäyttöliittymä. Käyttöliittymä on eristetty sovelluslogiikasta - kaikki tulostaminen ja käyttäjän kanssa kommunikointi tapahtuu ainoastaan käyttöliittymässä (*ui*). Käyttöliittymästä kutsutaan sovelluslogiikan, eli *GrocerylistServices*-luokan, metodeja.

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


Ohjelman rakennetta ja luokkien (GrocerylistService, GrocerylistRepository sekä Grocerylist) välisiä suhteita havainnollistetaan alla olevalla luokka-/pakkauskaaviolla:

![image](https://user-images.githubusercontent.com/78747844/206849601-bb0da61a-e4b1-4b31-a00e-e33fc79102e7.png)




## Sekvenssikaavio
### Tuotteen lisääminen
  
```mermaid
sequenceDiagram
  participant User
  participant UI
  participant GrocerylistService
  participant GrocerylistRepository
  participant Grocerylist
  User ->> UI: selects "lisää tuote"
  UI ->> GrocerylistService: add_product("maito", 2, "K-market")
  GrocerylistService ->> GrocerylistRepository  : find_product("maito","K-market")
  GrocerylistService ->> GrocerylistRepository: add(Grocerylist("maito", 2, "K-market"))
  GrocerylistRepository ->> Grocerylist: Grocerylist("maito", 2, "K-market")
  GrocerylistRepository -->> GrocerylistService: 
  GrocerylistService -->> UI:  
``` 
Toiminnallisuus alkaa käyttöliittymmässä, kun käyttäjä valitsee "lisää tuote" vaihtoehdon. Tämän jälkeen käyttäjä syöttää kaupan, tuotteen ja mahdollisen määrän. Käyttöliittymä kutsuu tämän jälkeen sovelluslogiikan *add_product* -metodia ja välittää annetut tiedot. Seuraavaksi sovelluslogiikka tarkastaa  *find_product* -metodilla onko ko.tuote jo ko.kaupan listassa. Mikäli näin ei ole (kuten tässä), niin sovelluslogiikka kutsuu seuraavaksi metodia *add(Grocerylist("maito", 2, "K-market"))*, joka lisää *Grocerylist("maito", 2, "K-market")*-olion tietokantaan. Tämä jälkeen kontrolli palaa takaisin käyttöliittymään.
