# main_pbo.py

# Mengimpor fungsi dan kelas dari modul lain
from modul_satu_pbo import hitung_luas_persegi, Lingkaran

def main():
    # Menguji fungsi hitung_luas_persegi
    sisi = 4  # Panjang sisi persegi
    luas_persegi = hitung_luas_persegi(sisi)  # Memanggil fungsi untuk menghitung luas
    print(f"Luas persegi dengan sisi {sisi} adalah: {luas_persegi}")  # Menampilkan hasil luas persegi

    # Menguji kelas Lingkaran
    jari_jari = 5  # Jari-jari lingkaran
    lingkaran = Lingkaran(jari_jari)  # Membuat objek Lingkaran dengan jari-jari tertentu
    luas_lingkaran = lingkaran.hitung_luas()  # Memanggil metode untuk menghitung luas lingkaran
    keliling_lingkaran = lingkaran.hitung_keliling()  # Memanggil metode untuk menghitung keliling lingkaran
    
    # Menampilkan hasil luas dan keliling lingkaran
    print(f"Luas lingkaran dengan jari-jari {jari_jari} adalah: {luas_lingkaran}")
    print(f"Keliling lingkaran dengan jari-jari {jari_jari} adalah: {keliling_lingkaran}")

# Memastikan bahwa fungsi main() hanya dijalankan jika file ini dieksekusi langsung
if __name__ == "__main__":
    main()  # Memanggil fungsi main()
