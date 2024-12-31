#  modul_satu_pbo.py

def operasi(a, b, op):
    if op == 'tambah':
        return a + b
    elif op == 'kurang':
        return a - b
    elif op == 'kali':
        return a * b
    elif op == 'bagi':
        return "Error: Pembagian dengan nol" if b == 0 else a / b
