# Nama : Moh. Dwi Afandi
# Kelas : XI TKJ 2
# Nomor Absen : 18
# Soal : Deskripsi Pekerjaan: Buatlah sebuah fungsi yang menghitung bilangan Fibonacci ke-n.
#        Rumus: Bilangan Fibonacci ke-n = Bilangan Fibonacci ke-(n-1) + Bilangan Fibonacci ke-(n-2)

def fibonacci(n):
    '''
    Program Python
    '''
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b


if __name__ == "__main__":
    try:
        input_n = int(input("Masukkan angka fibonacci: "))
    except ValueError as exc:
        raise exc
    
    print(f'Bilangan fibonacci dari {input_n} adalah {fibonacci(input_n)}')
