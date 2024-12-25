# main.py

from kalkulator import operasi

def main():
    print("Kalkulator Sederhana")
    print("Pilih operasi: tambah, kurang, kali, bagi")
    op = input("Masukkan operasi: ")
    a = float(input("Masukkan angka pertama: "))
    b = float(input("Masukkan angka kedua: "))
    
    hasil = operasi(a, b, op)
    print(f"Hasil: {hasil}")

if __name__ == "__main__":
    main()