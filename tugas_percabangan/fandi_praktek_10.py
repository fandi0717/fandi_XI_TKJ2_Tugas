# Nama      : Moh. Dwi Afandi
# Absen     : 18
# Kelas     : XI TKJ 2
# Soal      : Buat program Python yang mengambil nilai performa karyawan (1 hingga 5, dengan 5 sebagai 
#             performa terbaik) dan menghitung bonus tahunan berdasarkan aturan berikut:
#             • Performa 5: Bonus 20% dari gaji tahunan.
#             • Performa 4: Bonus 10% dari gaji tahunan.
#             • Performa 3: Bonus 5% dari gaji tahunan.
#             • Performa 2: Bonus 2% dari gaji tahunan.
#             • Performa 1: Tidak ada bonus.
#             Buatlah program menggunakan percabangan ternary untuk menghitung bonus tersebut

def main() -> str:
    '''
    Program Python
    --------------
    '''

    try:
        nilai_performa_karyawan = int(input("Nilai Performa Karyawan\t\t: "))
        gaji_tahunan = float(input("Gaji Tahunan Karyawan Tersebut\t: "))

    except ValueError as e:
        return f'Input Yang harus Anda Masukkah harus sesuai = {e}'

    assert 1 <= nilai_performa_karyawan <= 5, 'Nilai Performa Karyawan harus berada di antara 1 - 5'


    performa1 = 0 if nilai_performa_karyawan == 1 else 0
    performa2 = 2 / 100 * gaji_tahunan if nilai_performa_karyawan == 2 else performa1
    performa3 = 5 / 100 * gaji_tahunan if nilai_performa_karyawan == 3 else performa2
    performa4 = 10 / 100 * gaji_tahunan if nilai_performa_karyawan == 4 else performa3
    performa5 = 20 / 100 * gaji_tahunan if nilai_performa_karyawan == 5 else performa4

    total_gaji = gaji_tahunan + performa5

    return f'===========================================\nTotal Gaji Awal\t\t\t: {gaji_tahunan}\nBonus Tahunan sebesar\t\t: {performa5}\nTotal Gaji Akhir\t\t: {total_gaji}'

if __name__ == "__main__":
    print(main())
