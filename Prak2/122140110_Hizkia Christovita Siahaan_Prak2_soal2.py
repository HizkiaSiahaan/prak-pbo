import random

class PenaltyGame:
    def __init__(self, nama_pemain):
        self.nama_pemain = nama_pemain
        self.score = 0
        self.shots_taken = 0
        print(f"Selamat datang di game Penalty, {self.nama_pemain}!")

    def __del__(self):
        print(f"Terima kasih telah bermain, {self.nama_pemain}! Total tendangan yang dilakukan: {self.shots_taken}. Score: {self.score}.")

    def tendang(self, arah_tendangan):
        self.shots_taken += 1
        gol = random.choice([True, False])  
        if gol:
            self.score += 1
            print(f"GOOOOOOOOOL!!! {self.nama_pemain} mencetak gol!")
        else:
            print(f"{self.nama_pemain} menendang ke {arah_tendangan}, namun sayangnya masih melebar!")

def tampilkan_pesan(func):
    def wrapper(*args, **kwargs):
        print("Penendang bersiap untuk tendangan!")
        hasil = func(*args, **kwargs)
        print("Tendangan telah dilakukan!")
        return hasil
    return wrapper

class GamePenaltiDidekorasi(PenaltyGame):
    def tendang(self, arah_tendangan):
        return super().tendang(arah_tendangan)

def main():
    nama_pemain = input("Masukkan nama pemain: ")
    game = GamePenaltiDidekorasi(nama_pemain)

    while True:
        arah_tendangan = input("Pilih arah tendangan (kanan/kiri/tengah): ").lower()
        if arah_tendangan in ['kanan', 'kiri', 'tengah']:
            game.tendang(arah_tendangan)
        else:
            print("Arah tendangan tidak valid. Silakan pilih antara kanan, kiri, atau tengah.")

        lanjut = input("Apakah Anda ingin menendang lagi? (ya/tidak): ").lower()
        if lanjut != 'ya':
            break

if __name__ == "__main__":
    main()