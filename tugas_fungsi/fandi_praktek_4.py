# Nama : Moh. Dwi Afandi
# Kelas : XI TKJ 2
# Nomor Absen : 18
# Soal : Deskripsi Pekerjaan: Buatlah sebuah fungsi untuk menghitung jumlah digit dari suatu bilangan.
#        Rumus: Jumlah digit dari bilangan n = jumlah dari setiap digit dalam n

def hitung_jumlah_digit(bilangan: str) -> int | None:
    '''
    Program Python
    '''
    jml_digit = 0

    for digit in bilangan:
        if digit.isdigit():
            jml_digit += int(digit)
        else:
            return None

    return jml_digit

if __name__ == "__main__":
    input_n = input("Masukkan digit bilangan: ")
    
    print(f'Jumlah digit dari {input_n} adalah {hitung_jumlah_digit(input_n)}')
    