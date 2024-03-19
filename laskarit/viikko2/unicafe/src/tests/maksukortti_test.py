import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_alussa_oikein(self):
        self.assertEqual(self.maksukortti.saldo, 1000)
    
    def test_saldo_vahenee_oikein_jos_rahaa(self):
        kortti = Maksukortti(1000)
        nosto = kortti.ota_rahaa(500)
    
        self.assertEqual(kortti.saldo_euroina(), 5.0)
        self.assertTrue(nosto)
        

    def test_saldo_ei_vahene_jos_ei_tarpeeksi_rahaa(self):
        kortti = Maksukortti(500)
        nosto = kortti.ota_rahaa(1000)

        self.assertEqual(kortti.saldo_euroina(), 5.0)
        self.assertFalse(nosto)

    def test_saldo_lataa_oikein(self):
        kortti = Maksukortti(500)
        kortti.lataa_rahaa(1000)

        self.assertEqual(kortti.saldo_euroina(), 15.0)

        assert str(kortti) == "Kortilla on rahaa 15.00 euroa"


