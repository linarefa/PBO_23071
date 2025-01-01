# modul_satu_pbo.py 
#ini class test refa
# Fungsi untuk menghitung luas persegi
def hitung_luas_persegi(sisi):
    """Menghitung luas persegi berdasarkan panjang sisi."""
    return sisi * sisi  # Mengembalikan hasil luas persegi (sisi * sisi)

# Kelas untuk merepresentasikan sebuah Lingkaran
class Lingkaran:
    def __init__(self, jari_jari):
        """Inisialisasi objek Lingkaran dengan jari-jari tertentu."""
        self.jari_jari = jari_jari  # Menyimpan nilai jari-jari ke dalam atribut objek

    def hitung_luas(self):
        """Menghitung luas lingkaran."""
        return 3.14 * (self.jari_jari ** 2)  # Mengembalikan hasil luas lingkaran (π * r^2)

    def hitung_keliling(self):
        """Menghitung keliling lingkaran."""
        return 2 * 3.14 * self.jari_jari  # Mengembalikan hasil keliling lingkaran (2 * π * r)
