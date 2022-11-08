import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")    

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(2000)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 30.00 euroa")

    def test_rahan_ottaminen_menee_oikein_kun_rahaa_on_tarpeeksi(self):
        self.maksukortti.ota_rahaa(500)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 5.00 euroa")

    def test_rahan_ottaminen_menee_oikein_kun_rahaa_ei_ole_tarpeeksi(self):
        self.maksukortti.ota_rahaa(5000)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_rahat_riittaa(self):
        self.assertEqual(self.maksukortti.ota_rahaa(500), True)

    def test_rahat_ei_riita(self):
        self.assertEqual(self.maksukortti.ota_rahaa(5000), False)
        