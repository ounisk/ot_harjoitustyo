## Alustava luokka-/pakkauskaavio

![Luokka/pakkauskaavio](https://user-images.githubusercontent.com/78747844/204139577-442c7b10-9089-4a97-8fc7-bdb193b45609.png)



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
