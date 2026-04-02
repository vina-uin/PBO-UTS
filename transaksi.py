class ItemTransaksi:
    def __init__(self, barang, jumlah):
        # Yang divalidasi di sini adalah 'jumlah', bukan 'stok'
        if jumlah <= 0:
            raise ValueError("Jumlah harus lebih dari 0")

        self.nama_barang = barang.nama
        self.harga_saat_transaksi = barang.harga
        self.jumlah = jumlah

    def hitung_subtotal(self):
        return self.harga_saat_transaksi * self.jumlah

class Transaksi:
    def __init__(self):
        self.__items = []

    @property
    def items(self):
        return self.__items

    def tambah_item(self, barang, jumlah):
        barang.kurangi_stok(jumlah)
        item = ItemTransaksi(barang, jumlah)
        self.__items.append(item)

    def hitung_total(self):
        return sum(item.hitung_subtotal() for item in self.__items)