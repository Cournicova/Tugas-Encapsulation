class Karyawan:
    def __init__(self, id_karyawan, jabatan, kontrak, tahun_masuk):
        self.__id = id_karyawan
        self.__jabatan = jabatan
        self.kontrak = kontrak
        self.__tahun_masuk = tahun_masuk

    def get_id(self):
        return self.__id

    def set_id(self, id_baru):
        self.__id = id_baru

    def get_jabatan(self):
        return self.__jabatan

    def set_jabatan(self, jabatan_baru):
        self.__jabatan = jabatan_baru

    def get_tahun_masuk(self):
        return self.__tahun_masuk

    def set_tahun_masuk(self, tahun_masuk_baru):
        self.__tahun_masuk = tahun_masuk_baru

    def get_info(self):
        print(f"ID Karyawan : {self.__id}")
        print(f"Jabatan     : {self.__jabatan}")
        print(f"Kontrak     : {self.kontrak}")
        print(f"Tahun Masuk : {self.__tahun_masuk}")
    
    def laporan_keuangan(self, gaji, pengeluaran, pemasukan):
        print("Laporan Keuangan Perusahaan")
        print("----------------------------")
        print(f"Total Gaji Karyawan : {gaji}")
        print(f"Total Pengeluaran   : {pengeluaran}")
        print(f"Total Pemasukan     : {pemasukan}")
    
    def jadwal_kerja(self, jadwal_masuk, jadwal_libur):
        print("Jadwal Kerja Karyawan")
        print("-----------------------------")
        print(f"Jadwal Masuk: {jadwal_masuk}")
        print(f"Jadwal Libur: {jadwal_libur}")
        print()
        print(f"*"*50)

# Buat objek baru
karyawan4 = Karyawan("K004", "Keuangan", "Kontrak 2 tahun", 2021)

# Menampilkan objek baru
print(f"*"*40)
print("== Data Lama ==")
karyawan4.get_info()
print(f"*"*40)

# Mengakses properti private menggunakan getter
print(karyawan4.get_id()) # Output: K004
print(karyawan4.get_jabatan()) # Output: Keuangan
print(karyawan4.get_tahun_masuk()) # Output: 2021

# Mengubah properti private menggunakan setter
karyawan4.set_id("K005")
karyawan4.set_jabatan("HRD")
karyawan4.set_tahun_masuk(2022)

# Mengakses properti private yang sudah diubah menggunakan getter
print(karyawan4.get_id()) # Output: K005
print(karyawan4.get_jabatan()) # Output: HRD
print(karyawan4.get_tahun_masuk()) # Output: 2022

# Menampilkan objek baru
print(f"*"*40)
print("== Data Baru ==")
karyawan4.get_info()