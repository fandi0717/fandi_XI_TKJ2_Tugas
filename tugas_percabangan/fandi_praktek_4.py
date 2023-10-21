# Nama      : Moh. Dwi Afandi
# Absen     : 18
# Kelas     : XI TKJ 2
# Soal      : Buat program Python yang mengambil total belanjaan dan status anggota (biasa atau premium).
#             Berikan diskon berdasarkan aturan berikut:
#             • Anggota premium: Jika total belanjaan lebih dari 500.000, berikan diskon 15%. Jika tidak,
#             berikan diskon 10%.
#             • Anggota biasa: Jika total belanjaan lebih dari 300.000, berikan diskon 7%. Jika tidak, berikan
#             diskon 0%.



def main() -> str:
    '''
    Program Python
    --------------
    '''
    total_belanjaan = float(input("Total belanjaan Anda: "))
    status_anggota = input("Status anggota (Biasa/Premium): ").lower()

    if status_anggota == 'premium':
        if total_belanjaan > 500_000:
            diskon = total_belanjaan * 15 / 100
            hasil =  total_belanjaan - diskon
            return f'{"=" * 100}\nHarga Total Awal = {total_belanjaan} -------> Diskon(15%) = {diskon}\nHarga Total Akhir = {hasil}'

        else:
            diskon = total_belanjaan * 10 / 100
            hasil = total_belanjaan - diskon
            return f'{"=" * 100}\nHarga Total Awal = {total_belanjaan} -------> Diskon(10%) = {diskon}\nHarga Total Akhir = {hasil}'
        
    elif status_anggota == 'biasa':
        if total_belanjaan > 300_000:
            diskon = total_belanjaan * 7 / 100
            hasil = total_belanjaan - diskon
            return f'{"=" * 100}\nHarga Total Awal = {total_belanjaan} -------> Diskon(7%) = {diskon}\nHarga Total Akhir = {hasil}'
        else:
            return f'Total Harga Akhir : {total_belanjaan}'
    
    else:
        return f'{"="*100}\nKamu menginputkan status anggota yang salah'

        
if __name__ == "__main__":
    print(main())
