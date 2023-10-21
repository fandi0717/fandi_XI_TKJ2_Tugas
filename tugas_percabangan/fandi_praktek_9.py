# Nama      : Moh. Dwi Afandi
# Absen     : 18
# Kelas     : XI TKJ 2
# Soal      : Buat program Python yang mengambil durasi peminjaman buku dalam hari dan menentukan jenis 
#             pinjaman berdasarkan aturan berikut:
#             • Peminjaman 7 hari atau kurang: "Peminjaman Pendek"
#             • Peminjaman lebih dari 7 hari hingga 30 hari: "Peminjaman Menengah"
#             • Peminjaman lebih dari 30 hari: "Peminjaman Panjang"

def main() -> str:
    '''
    Program Python
    --------------
    '''

    try:
        input_user = int(input('Durasi Peminjaman Buku (hari) : '))

    except ValueError:
        return 'Input yang Anda masukkan harus berupa int'
    
    assert input_user > 0, 'Jumlah hari harus lebih besar dari 0'

    if input_user <= 7:
        return 'Peminjaman Pendek'
    
    elif 7 < input_user <= 30:
        return 'Peminjaman Menegah' 
    
    else:
        return 'Peminjaman Panjang'
    
if __name__ == "__main__":
    print(main())
