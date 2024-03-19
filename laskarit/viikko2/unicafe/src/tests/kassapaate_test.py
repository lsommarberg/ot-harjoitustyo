import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_luotu_kassapaate_init(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_syo_edullisesti_kateisella_toimii_kun_rahaa(self):
        kassapaate = Kassapaate()
        vaihtoraha = kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(kassapaate.edulliset, 1)
        self.assertEqual(vaihtoraha, 0)

    def test_syo_edullisesti_kateisella_toimii_kun_ei_rahaa(self):
        kassapaate = Kassapaate()
        vaihtoraha = kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(kassapaate.edulliset, 0)
        self.assertEqual(vaihtoraha, 200)

    def test_syo_maukkaasti_kateisella_toimii_kun_rahaa(self):
        kassapaate = Kassapaate()
        vaihtoraha = kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(kassapaate.kassassa_rahaa_euroina(), 1004.0)
        self.assertEqual(kassapaate.maukkaat, 1)
        self.assertEqual(vaihtoraha, 0)

    def test_syo_maukkaasti_kateisella_toimii_kun_ei_rahaa(self):
        kassapaate = Kassapaate()
        vaihtoraha = kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(kassapaate.maukkaat, 0)
        self.assertEqual(vaihtoraha, 200)

    def test_syo_maukkaasti_kortilla_toimii_kun_rahaa(self):
        kassapaate = Kassapaate()
        kortti = Maksukortti(500)
        osto = kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(kassapaate.maukkaat, 1)
        self.assertTrue(osto)

    def test_syo_maukkaasti_kortilla_toimii_kun_ei_rahaa(self):
        kassapaate = Kassapaate()
        kortti = Maksukortti(200)
        osto = kassapaate.syo_maukkaasti_kortilla(kortti)

        self.assertEqual(kassapaate.maukkaat, 0)
        self.assertFalse(osto)

    def test_syo_edullisesti_kortilla_toimii_kun_rahaa(self):
        kassapaate = Kassapaate()
        kortti = Maksukortti(500)
        osto = kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(kassapaate.edulliset, 1)
        self.assertTrue(osto)

    def test_syo_edullisesti_kortilla_toimii_kun_ei_rahaa(self):
        kassapaate = Kassapaate()
        kortti = Maksukortti(200)
        osto = kassapaate.syo_edullisesti_kortilla(kortti)

        self.assertEqual(kassapaate.edulliset, 0)
        self.assertFalse(osto)

    def test_lataa_rahaa_toimii_kun_summa_positiivinen(self):
        kassapaate = Kassapaate()
        kortti = Maksukortti(100)
        kassapaate.lataa_rahaa_kortille(kortti, 100)
        self.assertEqual(kortti.saldo, 200)
        self.assertEqual(kassapaate.kassassa_rahaa, 100100)

    def test_lataa_rahaa_toimii_kun_summa_negatiivinen(self):
        kassapaate = Kassapaate()
        kortti = Maksukortti(100)
        kassapaate.lataa_rahaa_kortille(kortti, -1)
        self.assertEqual(kortti.saldo, 100)
        self.assertEqual(kassapaate.kassassa_rahaa, 100000)