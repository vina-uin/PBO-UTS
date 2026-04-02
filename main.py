from datetime import date, datetime
from models.barang import Makanan, Minuman, KebutuhanRumahTangga
from models.transaksi import Transaksi
from models.toko import Toko

def tambah_data_awal(toko):
    """Fungsi pembantu untuk memasukkan data awal agar toko tidak kosong"""
    toko.tambah_barang(Makanan(nama="Roti", kategori="Makanan", harga=10000, stok=20, tanggal_kadaluarsa=date(2026, 1, 10)))
    toko.tambah_barang(Minuman(nama="Susu", kategori="Minuman", harga=12000, stok=15, tanggal_kadaluarsa=date(2026, 2, 20)))
    toko.tambah_barang(KebutuhanRumahTangga(nama="Sabun", kategori="Pembersih", harga=25000, stok=30, jenis="Cair", berbahaya=True))

def menu_tambah_barang(toko):
    """Sub-menu khusus untuk Admin menambahkan barang baru ke inventaris"""
    print("\n--- ADMIN: TAMBAH BARANG BARU ---")
    print("Pilih Kategori Barang:")
    print("1. Makanan")
    print("2. Minuman")
    print("3. Kebutuhan Rumah Tangga")
    
    jenis_pilihan = input("Pilih kategori (1/2/3): ")
    if jenis_pilihan not in ['1', '2', '3']:
        print("Pilihan kategori tidak valid.")
        return

    try:
        nama = input("Masukkan Nama Barang: ")
        harga = int(input("Masukkan Harga: Rp "))
        stok = int(input("Masukkan Jumlah Stok: "))

        # Logika untuk barang yang memiliki tanggal kadaluarsa (Makanan & Minuman)
        if jenis_pilihan in ['1', '2']:
            kategori = "Makanan" if jenis_pilihan == '1' else "Minuman"
            tgl_str = input("Masukkan Tanggal Kadaluarsa (Format YYYY-MM-DD, misal 2026-12-31): ")
            
            # Mengubah teks string menjadi objek format Date Python
            tgl_kadaluarsa = datetime.strptime(tgl_str, "%Y-%m-%d").date()
            
            if jenis_pilihan == '1':
                barang_baru = Makanan(nama, kategori, harga, stok, tgl_kadaluarsa)
            else:
                barang_baru = Minuman(nama, kategori, harga, stok, tgl_kadaluarsa)
                
        # Logika untuk barang Kebutuhan Rumah Tangga
        elif jenis_pilihan == '3':
            kategori = input("Masukkan Kategori (misal: Pembersih, Alat Dapur): ")
            jenis = input("Masukkan Jenis (misal: Cair, Padat, Gas): ")
            input_bahaya = input("Apakah barang ini berbahaya/mengandung kimia keras? (y/n): ")
            is_berbahaya = True if input_bahaya.lower() == 'y' else False
            
            barang_baru = KebutuhanRumahTangga(nama, kategori, harga, stok, jenis, is_berbahaya)
        
        # Memasukkan objek yang sudah jadi ke dalam sistem toko
        toko.tambah_barang(barang_baru)
        print(f"\nukses! {nama} berhasil ditambahkan ke rak toko.")
        
    except ValueError as e:
        print("\n GAGAL: Input tidak valid. Pastikan harga/stok berupa angka dan format tanggal benar.")
        print(f"Detail error: {e}")

def menu_kasir(toko):
    #Sub-menu khusus untuk memproses transaksi pelanggan
    print("\n--- KASIR: PROSES TRANSAKSI ---")
    transaksi = Transaksi()
    
    while True:
        cari_nama = input("Masukkan nama barang (atau ketik 'bayar' / 'batal'): ")
        
        if cari_nama.lower() == 'bayar':
            break
        if cari_nama.lower() == 'batal':
            print("Transaksi dibatalkan.")
            return

        barang = toko.cari_barang(cari_nama)
        
        if barang:
            try:
                jumlah = int(input(f"Berapa banyak {barang.nama} yang dibeli? : "))
                transaksi.tambah_item(barang, jumlah) 
                print(f"Masuk keranjang: {jumlah} {barang.nama}\n")
            except ValueError as e:
                print(f" GAGAL: {e}\n")
        else:
            print("Barang tidak ditemukan!\n")

    if transaksi.items:
        toko.proses_transaksi(transaksi)
        print("\n" + "="*30)
        print("         STRUK BELANJA         ")
        print("="*30)
        for item in transaksi.items:
            print(f"{item.nama_barang:<15} x{item.jumlah:<3} : Rp {item.hitung_subtotal():>7}")
        print("-" * 30)
        print(f"TOTAL KESELURUHAN : Rp {transaksi.hitung_total():>7}")
        print("="*30 + "\n")
    else:
        print("Tidak ada barang yang dibeli.")

def main():
    toko = Toko()
    tambah_data_awal(toko) 

    while True:
        print("\n" + "="*40)
        print("SISTEM MANAJEMEN TOKO SWALAYAN ")
        print("="*40)
        print("1. Lihat Daftar Barang")
        print("2. Proses Transaksi (Kasir)")
        print("3. Laporan Sisa Stok Akhir")
        print("4. Laporan Riwayat Transaksi")
        print("5. Tambah Barang Baru (Admin)")
        print("0. Keluar Aplikasi")
        print("="*40)
        
        pilihan = input("Pilih menu (0-5): ")

        if pilihan == '1':
            print("\n--- DAFTAR BARANG TERSEDIA ---")
            for barang in toko.get_daftar_barang():
                print(f"- {barang.info()} | Harga: Rp{barang.harga} | Sisa Stok: {barang.stok}")
                
        elif pilihan == '2':
            menu_kasir(toko)
            
        elif pilihan == '3':
            print("\n--- LAPORAN STOK BARANG ---")
            for nama, stok in toko.laporan_stok():
                print(f"{nama:<20} : {stok:>3} pcs")
                
        elif pilihan == '4':
            print("\n--- LAPORAN RIWAYAT TRANSAKSI ---")
            riwayat = toko.laporan_transaksi()
            if not riwayat:
                print("Belum ada transaksi hari ini.")
            else:
                for i, daftar_item in enumerate(riwayat, 1):
                    print(f"Transaksi #{i}:")
                    for nama, jumlah in daftar_item:
                        print(f"  > {nama} (x{jumlah})")
                        
        elif pilihan == '5':
            menu_tambah_barang(toko)

        elif pilihan == '0':
            print("\nSistem ditutup. Terima kasih!")
            break 
            
        else:
            print("\nPilihan tidak valid!")

if __name__ == "__main__":
    main()