```mermaid
classDiagram
  Peli "1" -- "1" Pelilauta
  Peli "1" -- "2-8" Pelaaja
  Pelilauta "1" -- "40" Ruudut
  Ruudut "1" -- "0-8" Nappula
  Nappula "1" -- "1" Pelaaja
  Nopat "2" -- "1" Peli
```  
  
