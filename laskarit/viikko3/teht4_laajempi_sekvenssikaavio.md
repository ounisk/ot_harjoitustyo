```mermaid
sequenceDiagram
  participant main
  participant laitehallinto
  participant rautatietori
  participant ratikka6
  participant bussi244
  participant lippu_luukku
  participant kalle_kortti
  main ->> laitehallinto: lisää_lataaja(rautatietori)
  laitehallinto ->> rautatietori: append(rautatietori)
  main ->> laitehallinto: lisää_lukija(ratikka6)
  laitehallinto ->> ratikka6: append(ratikka6)
  main ->> laitehallinto: lisää_lukija(bussi244)
  laitehallinto ->> bussi244: append(bussi244)
 
