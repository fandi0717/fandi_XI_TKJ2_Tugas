# Nama : Moh. Dwi Afandi
# Kelas : XI TKJ 2
# Nomor Absen : 18
# Soal : Deskripsi Pekerjaan: Seorang petani memiliki 100 ekor ayam di peternakannya. Setiap bulan, jumlah
#        ayam bertambah 5% dari jumlah ayam pada bulan sebelumnya. Buatlah program yang menghitung
#        berapa bulan yang dibutuhkan agar jumlah ayam melebihi 200 ekor.
#        Rumus: Jumlah ayam bulan ke-n = Jumlah ayam bulan ke-(n-1) + 5% dari Jumlah ayam bulan ke-(n-1)


def main() -> int:
    '''
    Program Python
    '''
    jumlah_ayam = 100
    total_bulan = 0
 
    while jumlah_ayam <= 200:
        jumlah_ayam += (jumlah_ayam * 0.05)
        total_bulan += 1

    return total_bulan

if __name__ == "__main__":
    print(f'Jumlah bulan yang dibutuhkan untuk melebihi 200 ekor ayam adalah {main()} bulan')
