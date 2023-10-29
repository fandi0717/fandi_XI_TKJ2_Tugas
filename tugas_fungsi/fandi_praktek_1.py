# Nama : Moh. Dwi Afandi
# Kelas : XI TKJ 2
# Nomor Absen : 18
# Soal : Deskripsi Pekerjaan: Buatlah sebuah fungsi yang menghitung total dari deret bilangan ganjil hingga
#        batas tertentu yang ditentukan pengguna.
#        Rumus: Total deret bilangan ganjil = 1 + 3 + 5 + ... + (2n-1)


def total_deret_bilangan_ganjil(n: int) -> int:
    '''
    Program Python
    '''
    
    item_ganjil = []

    for i in range(n + 1):
        if i % 2 == 1:
            item_ganjil.append(i)

    return sum(item_ganjil)

if __name__ == "__main__":
    try:
        n_input = int(input("Masukkan angka batas: "))
    except ValueError as exc:
        raise exc
    print(f'Total deret bilangan ganjil dengan batas {n_input} adalah {total_deret_bilangan_ganjil(n_input)}')
