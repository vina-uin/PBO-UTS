from abc import ABC, abstractmethod
from datetime import datetime

class Barang(ABC):
    def __init__(self, nama, kategori, harga, stok):
        if harga <= 0:
            raise ValueError("Harga harus lebih dari 0")
        if stok < 0:
            raise ValueError("Stok tidak boleh negatif")
            
        self.nama = nama
        self.kategori = kategori
        self.__harga = harga
        self.__stok = stok

    @property
    def harga(self):
        return self.__harga

    @property
    def stok(self):
        return self.__stok

    def kurangi_stok(self, jumlah):
        if jumlah <= 0:
            raise ValueError("Jumlah stok harus lebih besar dari 0.")
        if jumlah > self.__stok:
            raise ValueError("Stok tidak mencukupi")
        self.__stok -= jumlah

    def tambah_stok(self, jumlah):
        if jumlah <= 0:
            raise ValueError("Jumlah harus lebih dari 0")
        self.__stok += jumlah
    
    @abstractmethod
    def info(self):
        pass

class BarangKadaluarsa(Barang):
    def __init__(self, nama, kategori, harga, stok, tanggal_kadaluarsa):
        super().__init__(nama, kategori, harga, stok)
        self.tanggal_kadaluarsa = tanggal_kadaluarsa

    def cek_kadaluarsa(self):
        return datetime.now().date() > self.tanggal_kadaluarsa

class Makanan(BarangKadaluarsa):
    def info(self):
        return f"Makanan: {self.nama}"

class Minuman(BarangKadaluarsa):
    def info(self):
        return f"Minuman: {self.nama}"

class KebutuhanRumahTangga(Barang):
    def __init__(self, nama, kategori, harga, stok, jenis, berbahaya=False):
        super().__init__(nama, kategori, harga, stok)
        self.jenis = jenis
        self.berbahaya = berbahaya

    def info(self):
        return f"Kebutuhan Rumah Tangga: {self.nama} ({self.jenis})"