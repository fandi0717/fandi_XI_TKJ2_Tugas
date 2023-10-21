# Nama      : Moh. Dwi Afandi
# Absen     : 18
# Kelas     : XI TKJ 2
# Soal      : Buat program Python yang mengambil data penjualan bulanan produk dan menentukan kategori
#             produk berdasarkan penjualan:
#             • Jika penjualan lebih dari 1000 unit, kategorikan sebagai "Produk Terlaris."
#             • Jika penjualan antara 500 hingga 1000 unit, kategorikan sebagai "Produk Populer."
#             • Jika penjualan kurang dari 500 unit, kategorikan sebagai "Produk Biasa."


def main() -> str:
    '''
    Program Python
    ---------------
    '''
    input_data_penjualan = float(input('Masukkan Data Penjualan: '))

    if input_data_penjualan > 1000:
        return f'{"=" * 100}\nProduk Terlaris'
    elif 500 <= input_data_penjualan <= 1000:
        return f'{"=" * 100}\nProduk Populer'
    else:
        return f'{"=" * 100}\nProduk Biasa'

if __name__ == "__main__":
    print(main())
    