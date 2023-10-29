# Nama : Moh. Dwi Afandi
# Kelas : XI TKJ 2
# Nomor Absen : 18
# Soal : Deskripsi Pekerjaan: Sebuah investasi awal sebesar 10.000 dollar tumbuh sebesar 6% setiap
#        tahunnya. Buatlah program yang menghitung berapa tahun yang dibutuhkan agar nilai investasi
#        melebihi 20.000 dollar.
#        Rumus: Nilai investasi tahun ke-n = Nilai investasi tahun ke-(n-1) + 6% dari Nilai investasi tahun ke-(n-1)


def main() -> int:
    '''
    Program Python
    '''
    investasi_awal = 10_000
    jumlah_tahun = 0

    while investasi_awal <= 20_000:
        investasi_awal += (investasi_awal * 6 / 100)
        jumlah_tahun += 1

    return jumlah_tahun

if __name__ == "__main__":
    print(f'Agar nilai investasi melebih 20.000 dolar, maka membutuhkan : {main()} tahun')
