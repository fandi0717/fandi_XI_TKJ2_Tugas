# Nama      : Moh. Dwi Afandi
# Absen     : 18
# Kelas     : XI TKJ 2
# Soal      : Buat program Python yang mengambil status persiapan proyek dan menentukan apakah proyek 
#             tersebut dapat diluncurkan. Jika status persiapan "Siap," program harus mencetak "Proyek 
#             diluncurkan." Jika status persiapan "Tunda," program harus mencetak "Proyek ditunda."


def main() -> str:
    '''
    Program Python
    --------------
    '''
    pembuka = '''
Bagaimana Status Persiapan Proyek ? -> [Siap, Tunda]'''

    input_user = input(f'{pembuka} : ').lower()

    if input_user == 'siap':
        return '======================\nProyek diluncurkan'
    elif input_user == 'tunda':
        return '======================\nProyek ditunda'
    else:
        return 'Error : Your input must be "Siap" or "Tunda"'


if __name__ == "__main__":
    print(main())
