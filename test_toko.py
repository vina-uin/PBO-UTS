import unittest
from datetime import date
from models.barang import Makanan
from models.transaksi import Transaksi
from models.toko import Toko


class TestToko(unittest.TestCase):

    def setUp(self):
        self.toko = Toko()
        self.barang = Makanan("Roti", "Makanan", 10000, 10, date(2026, 1, 1))
        self.toko.tambah_barang(self.barang)

    def test_stok_berkurang(self):
        transaksi = Transaksi()
        transaksi.tambah_item(self.barang, 2)
        self.assertEqual(self.barang.stok, 8)

    def test_stok_tidak_cukup(self):
        transaksi = Transaksi()
        with self.assertRaises(ValueError):
            transaksi.tambah_item(self.barang, 20)

    def test_total_transaksi(self):
        transaksi = Transaksi()
        transaksi.tambah_item(self.barang, 2)
        self.assertEqual(transaksi.hitung_total(), 20000)

    def test_laporan_transaksi(self):
        transaksi = Transaksi()
        transaksi.tambah_item(self.barang, 2)
        self.toko.proses_transaksi(transaksi)

        laporan = self.toko.laporan_transaksi()
        self.assertEqual(laporan[0][0][1], 2)


if __name__ == "__main__":
    unittest.main()