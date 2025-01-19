class KlinikAntrian:
    def _init_(self):
        """Inisialisasi daftar antrian dan log pasien."""
        self.antrian = [
            {"nama": "Jisoo", "keluhan": "Flu"},
            {"nama": "Jennie", "keluhan": "Demam"},
            {"nama": "Rose", "keluhan": "Sakit Perut"}
        ]  # Daftar pasien awal
        self.log = []  # Log pasien yang sudah dilayani

    def tambah_pasien(self, nama_pasien, keluhan):
        """Menambahkan pasien ke dalam antrian."""
        self.antrian.append({"nama": nama_pasien, "keluhan": keluhan})
        print(f"\nPasien '{nama_pasien}' dengan keluhan '{keluhan}' telah ditambahkan ke antrian.")

    def panggil_pasien(self):
        """Memanggil pasien pertama dari antrian."""
        if self.antrian:
            pasien_dipanggil = self.antrian.pop(0)
            print(f"\nMemanggil pasien: {pasien_dipanggil['nama']}")
            print(f"Keluhan: {pasien_dipanggil['keluhan']}")
            self.log.append(pasien_dipanggil)  # Pindahkan ke log setelah dipanggil
        else:
            print("\nTidak ada pasien dalam antrian.")

    def lihat_antrian(self):
        """Menampilkan daftar pasien yang sedang mengantri."""
        if self.antrian:
            print("\nDaftar antrian saat ini:")
            for i, pasien in enumerate(self.antrian, start=1):
                print(f"{i}. {pasien['nama']} - Keluhan: {pasien['keluhan']}")
        else:
            print("\nTidak ada pasien dalam antrian.")

    def lihat_log(self):
        """Menampilkan log pasien yang sudah dilayani."""
        if self.log:
            print("\nLog pasien yang sudah dilayani:")
            for i, pasien in enumerate(self.log, start=1):
                print(f"{i}. {pasien['nama']} - Keluhan: {pasien['keluhan']}")
        else:
            print("\nBelum ada pasien yang dilayani.")

    def jalankan(self):
        """Menjalankan sistem manajemen antrian."""
        while True:
            print("\n=== Sistem Manajemen Antrian Klinik ===")
            print("1. Tambah Pasien")
            print("2. Panggil Pasien Berikutnya")
            print("3. Lihat Daftar Antrian")
            print("4. Lihat Log Pasien Dilayani")
            print("5. Keluar")
            pilihan = input("Pilih menu (1-5): ")

            if pilihan not in ["1", "2", "3", "4", "5"]:
                print("\nPilihan tidak valid. Silakan coba lagi.")
                continue

            if pilihan == "1":
                nama_pasien = input("Masukkan nama pasien: ").strip()
                keluhan = input("Masukkan keluhan pasien: ").strip()
                self.tambah_pasien(nama_pasien, keluhan)
            elif pilihan == "2":
                self.panggil_pasien()
            elif pilihan == "3":
                self.lihat_antrian()
            elif pilihan == "4":
                self.lihat_log()
            elif pilihan == "5":
                print("\nTerima kasih telah menggunakan sistem ini. Sampai jumpa!")
                break


# Jalankan program
if __name__ == "__main__":
    # Membuat instance dari kelas KlinikAntrian
    sistem_antrian = KlinikAntrian()

    # Menjalankan sistem
    sistem_antrian.jalankan()