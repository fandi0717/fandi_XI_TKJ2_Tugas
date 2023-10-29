# Nama : Moh. Dwi Afandi
# Kelas : XI TKJ 2
# Nomor Absen : 18
# Soal : Deskripsi Pekerjaan: Seorang pedagang memiliki 100 buah apel. Setiap harinya, ia menjual 10% dari
#        jumlah apel yang tersisa. Buatlah program yang menghitung berapa hari yang dibutuhkan agar sisa
#        apel kurang dari 20 buah.
#        Rumus: Sisa apel hari ke-n = Sisa apel hari ke-(n-1) - 10% dari Sisa apel hari ke-(n-1)

def main() -> int:
    '''
    Program Python
    '''
    jumlah_awal_apel = 100
    total_hari = 0

    while jumlah_awal_apel >= 20:
        jumlah_awal_apel -= (jumlah_awal_apel * 10 / 100)
        total_hari += 1

    return total_hari

if __name__ == "__main__":
    print(f'Jumlah hari yang dibutuhkan agar sisa apel kurang dari 20 adalah {main()} hari')
