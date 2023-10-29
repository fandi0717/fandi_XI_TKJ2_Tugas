# Nama : Moh. Dwi Afandi
# Kelas : XI TKJ 2
# Nomor Absen : 18
# Soal : Deskripsi Pekerjaan: Seorang pelari ingin meningkatkan jarak tempuhnya setiap minggunya. Ia mulai
#        dengan 5 kilometer dan meningkatkan jaraknya sebesar 10% setiap minggunya. Buatlah program
#        yang menghitung berapa minggu yang dibutuhkan agar pelari itu dapat berlari lebih dari 10
#        kilometer.
#        Rumus: Jarak minggu ke-n = Jarak minggu ke-(n-1) + 10% dari Jarak minggu ke-(n-1)

def main() -> int:
    '''
    Program Python
    '''
    lari_awal = 5
    total_minggu = 0

    while lari_awal <= 10:
        lari_awal += (lari_awal * 10 / 100)
        total_minggu += 1

    return total_minggu

if __name__ == "__main__":
    print(f'Agar pelari bisa berlari lebih dari 10 km, maka pelari membutuhkan : {main()} minggu')
