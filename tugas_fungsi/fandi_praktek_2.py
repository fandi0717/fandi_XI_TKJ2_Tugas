# Nama : Moh. Dwi Afandi
# Kelas : XI TKJ 2
# Nomor Absen : 18
# Soal : Deskripsi Pekerjaan: Buatlah sebuah fungsi untuk menghitung faktorial dari suatu bilangan.
#        Rumus: Faktorial n = n * (n-1) * (n-2) * ... * 1

from typing import Any  

def factorial(n: int) -> Any:
    '''
    Program Python
    '''
    
    if n < 0:
        return "Angka yang anda masukkan harus positif"
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == "__main__":
    try:
        input_n = int(input("Masukkan angka faktorial: "))
    except ValueError as exc:
        raise exc
    
    if isinstance(factorial(input_n), str):
        print(factorial(input_n))
    else:
        print(f'Faktorial dari {input_n} = {factorial(input_n)}')
