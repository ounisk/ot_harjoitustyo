import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.edulliset = 0
        self.maukkaat = 0
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kassapaate_saldo_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)    

    def test_luotu_kassapaate_edulliset_lounaat_oikein(self):
        self.assertEqual(self.edulliset, 0) 

    def test_luotu_kassapaate_maukkaat_lounaat_oikein(self):
        self.assertEqual(self.maukkaat, 0)   

    def test_kateisosto_edullinen_maksu_riittaa_kassatilanne(self):
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_kateisosto_edullinen_maksu_riittaa_myydyt_lounaat(self):
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.edulliset, 1) 

    def test_kateisosto_edullinen_maksu_riittaa_vaihtorahat(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(500), 260)    

    def test_kateisosto_edullinen_maksu_ei_riita_kassatilanne(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)    

    def test_kateisosto_edullinen_maksu_ei_riita_myydyt_lounaat(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.edulliset, 0)  

    def test_kateisosto_edullinen_maksu_ei_riita_vaihtorahat(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(100), 100)    
        
    def test_kateisosto_maukas_maksu_riittaa_kassatilanne(self):
        self.kassapaate.syo_maukkaasti_kateisella(1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_kateisosto_maukas_maksu_riittaa_myydyt_lounaat(self):
        self.kassapaate.syo_maukkaasti_kateisella(1000)
        self.assertEqual(self.kassapaate.maukkaat, 1) 

    def test_kateisosto_maukas_maksu_riittaa_vaihtorahat(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(1000), 600)    

    def test_kateisosto_maukas_maksu_ei_riita_kassatilanne(self):
        self.kassapaate.syo_maukkaasti_kateisella(399)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)    

    def test_kateisosto_maukas_maksu_ei_riita_myydyt_lounaat(self):
        self.kassapaate.syo_maukkaasti_kateisella(399)
        self.assertEqual(self.kassapaate.maukkaat, 0)     

    def test_kateisosto_maukas_maksu_ei_riita_vaihtorahat(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(399), 399)     



    def test_korttiosto_edullinen_saldo_riittaa_palauttaa_True(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)

    def test_korttiosto_edullinen_saldo_ei_riita_palauttaa_False(self):#
        self.maksukortti = Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), False)

    def test_korttiosto_edullinen_saldo_riittaa_kortin_saldo_muuttuu_oikein(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 7.60 euroa")

    def test_korttiosto_edullinen_saldo_ei_riita_kortin_saldo_ei_muutu(self):
        self.maksukortti = Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 2.00 euroa")    

    def test_korttiosto_edullinen_saldo_riittaa_myydyt_lounaat(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_korttiosto_edullinen_saldo_ei_riita_myydyt_lounaat_ei_muutu(self): 
        self.maksukortti = Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_korttiosto_edullinen_saldo_riittaa_eika_kassa_muutu(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

   
    def test_korttiosto_maukas_saldo_riittaa_palauttaa_True(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)

    def test_korttiosto_maukas_saldo_ei_riita_palauttaa_False(self):#
        self.maksukortti = Maksukortti(399)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), False)

    def test_korttiosto_maukas_saldo_riittaa_kortin_saldo_muuttuu_oikein(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 6.00 euroa")

    def test_korttiosto_maukas_saldo_ei_riita_kortin_saldo_ei_muutu(self): 
        self.maksukortti = Maksukortti(399)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 3.99 euroa")    

    def test_korttiosto_maukas_saldo_riittaa_myydyt_lounaat(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_korttiosto_maukas_saldo_ei_riita_myydyt_lounaat_ei_muutu(self):
        self.maksukortti = Maksukortti(399)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_korttiosto_maukas_saldo_riittaa_eika_kassa_muutu(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)  

  
    def test_lataa_rahaa_kortin_saldo_muuttuu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 500)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 15.00 euroa")

    def test_lataa_neg_rahaa_kortin_saldo_ei_muuttuu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")    

    def test_lataa_rahaa_kassan_saldo_muuttuu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100500)

    def test_lataa_neg_rahaa_kassan_saldo_ei_muutu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)  

