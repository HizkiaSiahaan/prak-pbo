class Jualan:
    jumlah_barang = 0
    list_barang = []

    def __init__(self, nama, stok, harga):
        self.__nama = nama
        self.__stok = stok
        self.__harga = harga
        Jualan.jumlah_barang += 1
        Jualan.list_barang.append((nama, stok, harga))

    def lihat_barang():
        print("Jumlah barang yang di jual pada toko:", Jualan.jumlah_barang, "buah")
        for i, barang in enumerate(Jualan.list_barang, 1):
            nama, stok, harga = barang
            print(f"{i}. {nama} seharga Rp {harga} (stok: {stok})")

    def __del__(self):
        Jualan.jumlah_barang -= 1
        for i, barang in enumerate(Jualan.list_barang):
            nama, _, _ = barang
            if nama == self.__nama:
                del Jualan.list_barang[i]
                print(f"{self.__nama} dihapus dari toko!")
                break

# Contoh penggunaan
Jualan1 = Jualan("Galon Aqua 19L", 32, 17000)
Jualan2 = Jualan("Gas LPG 5 kg", 22, 88000)
Jualan3 = Jualan("Beras Ramos 5 kg", 13, 68000)
Jualan.lihat_barang()

del Jualan1
Jualan.lihat_barang()