from mixins.laporan import LaporanMixin

class Toko(LaporanMixin):
    def __init__(self):
        self._daftar_barang = []
        self._riwayat_transaksi = []

    def tambah_barang(self, barang):
        self._daftar_barang.append(barang)

    def hapus_barang(self, nama):
        self._daftar_barang = [b for b in self._daftar_barang if b.nama != nama]

    def cari_barang(self, nama):
        for barang in self._daftar_barang:
            if barang.nama == nama:
                return barang
        return None

    def proses_transaksi(self, transaksi):
        self._riwayat_transaksi.append(transaksi)

    def get_daftar_barang(self):
        return self._daftar_barang