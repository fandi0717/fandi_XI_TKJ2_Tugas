# Nama      : Moh. Dwi Afandi
# Absen     : 18
# Kelas     : XI TKJ 2
# Soal      : Buat program Python yang mengambil informasi pembaruan perangkat lunak dan menentukan
#             apakah sistem perlu di-restart. Jika pembaruan mengharuskan restart, program harus mencetak
#             "Sistem perlu di-restart." Jika tidak, program harus mencetak "Sistem tidak perlu di-restart."


def main() -> str:
    '''
    Program Python
    ==============
    '''
    pembuka = '''
=============================================================
Komputer Anda telah menerima pembaruan Perangkat Lunak.
=============================================================
Apakah pesan yang muncul dari pembaruan Perangkat Lunak tersebut :
[1] Restart Your Computer
[0] Don't need Restart Your Computer
    '''
    print(pembuka)

    input_user = int(input('Ketikkan angka sesuai dengan informasi yang muncul di display Anda: '))

    jawaban = '='*61

    if input_user == 1:
        return f'{jawaban}\nAnswer: Sistem perlu di-restart'
    elif input_user == 0:
        return f'{jawaban}\nAnswer: Sistem tidak perlu di-restart'
    
    else:
        return 'Error : Input Yang Anda masukkan salah: (0, 1)'

    

if __name__ == "__main__":
    print(main())
