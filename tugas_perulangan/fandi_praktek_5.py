# Nama : Moh. Dwi Afandi
# Kelas : XI TKJ 2
# Nomor Absen : 18
# Soal : Deskripsi Pekerjaan: Sebuah bakteri pembelahan setiap 20 menit. Sebuah bakteri ditempatkan
#        dalam lingkungan yang cocok dan berkembang biak dengan cepat. Buatlah program yang
#        menghitung berapa kali pembelahan bakteri terjadi dalam rentang waktu 2 jam.
#        Rumus: Jumlah pembelahan setelah t menit = t / 20

def main() -> int:
    '''
    Program Python
    '''
    total_waktu = 120 # 2 jam
    waktu_pembelahan = 20 

    jml_pembelahan = total_waktu // waktu_pembelahan

    return jml_pembelahan

if __name__ == "__main__":
    print(f"Jumlah pembelahan bakteri dalam rentang waktu 2 jam : {main()} kali")
