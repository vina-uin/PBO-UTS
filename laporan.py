class LaporanMixin:
    def laporan_stok(self):
        return [(barang.nama, barang.stok) for barang in self._daftar_barang]

    def laporan_transaksi(self):
        hasil = []
        for t in self._riwayat_transaksi:
            hasil.append([(item.nama_barang, item.jumlah) for item in t.items])
        return hasil