# Nama : Moh. Dwi Afandi
# Kelas : XI TKJ 2
# Nomor Absen : 18
# Soal : Deskripsi Pekerjaan: Buatlah sebuah fungsi yang menghitung nilai pangkat dari suatu bilangan
#        dengan eksponen tertentu.
#        Rumus: Bilangan^Eksponen

from typing import Any

def pangkat(bilangan, exp) -> Any:
    '''
    Program Python
    '''
    return pow(bilangan, exp)

if __name__ == "__main__":
    try:
        input_bil = float(input("Masukkan bilangan (base): "))
        input_exp = float(input("Masukkan bilangan (base): "))
    except ValueError as exc:
        raise exc
    
    if input_bil.is_integer():
        input_bil = int(input_bil)
    if input_exp.is_integer():
        input_exp = int(input_exp)
    
    print(f'{input_bil} ** {input_exp} = {pangkat(input_bil, input_exp)}')
