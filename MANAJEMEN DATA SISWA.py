class Siswa:
    def __init__(self, nama, usia, nilai):
        self.nama = nama
        self.usia = usia
        self.nilai = nilai

    def __str__(self):
        return f"Nama: {self.nama} Usia: {self.usia} Nilai Rata-Rata: {self.nilai}"

class Manajemen:
    def __init__(self):
        self.daftar_siswa = []

    def tambah_siswa(self):
        nama = input("Masukkan Nama Siswa: ")
        usia = int(input("Masukkan Usia Siswa: "))
        nilai = float(input("Masukkan Nilai Rata-Rata: "))
        self.daftar_siswa.append(Siswa(nama, usia, nilai))
        print("Siswa Telah Ditambahkan \n")

    def lihat_siswa(self):
        if not self.daftar_siswa:
            print("Belum ada data siswa.\n")
        else:
            for idx, siswa in enumerate(self.daftar_siswa, start=1):
                print(f"{idx}. {siswa}")
            print()

    def edit_siswa(self):
        self.lihat_siswa()
        indeks = int(input("Masukkan Indeks Siswa Yang Ingin Diedit: ")) - 1
        if 0 <= indeks < len(self.daftar_siswa):
            self.daftar_siswa[indeks].nama = input("Masukkan Nama Yang Baru: ")
            self.daftar_siswa[indeks].usia = int(input("Masukkan Usia Yang Baru: "))
            self.daftar_siswa[indeks].nilai = float(input("Masukkan Nilai Rata-Rata Yang Baru: "))
            print("Data Siswa Telah Diperbarui \n")
        else:
            print("Indeks Tidak Valid \n")

    def hapus_siswa(self):
        self.lihat_siswa()
        indeks = int(input("Masukkan Indeks Siswa Yang Ingin Dihapus: ")) - 1
        if 0 <= indeks < len(self.daftar_siswa):
            del self.daftar_siswa[indeks]
            print("Siswa Berhasil Dihapus \n")
        else:
            print("Indeks Tidak Valid \n")

    def cari_siswa(self):
        nama = input("Masukkan Nama Siswa Yang Ingin Dicari: ")
        hasil = [siswa for siswa in self.daftar_siswa if siswa.nama.lower() == nama.lower()]
        if hasil:
            for siswa in hasil:
                print(siswa)
        else:
            print("Siswa Tidak Ditemukan")

    def tampilkan_menu(self):
        while True:
            print("\n Menu Manajemen Data Siswa: ")
            print("1. Tambah Siswa")
            print("2. Lihat Daftar Siswa")
            print("3. Edit Data Siswa")
            print("4. Hapus Siswa")
            print("5. Cari Siswa")
            print("6. Keluar")
            pilihan = input("Pilih Opsi (1-6): ")

            if pilihan == '1':
                self.tambah_siswa()
            elif pilihan == '2':
                self.lihat_siswa()
            elif pilihan == '3':
                self.edit_siswa()
            elif pilihan == '4':
                self.hapus_siswa()
            elif pilihan == '5':
                self.cari_siswa()
            elif pilihan == '6':
                print("Terima kasih!")
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.\n")

# Jalankan program
if __name__ == "__main__":
    manajemen = Manajemen()
    manajemen.tampilkan_menu()
