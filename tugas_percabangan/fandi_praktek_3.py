# Nama      : Moh. Dwi Afandi
# Absen     : 18
# Kelas     : XI TKJ 2
# Soal      : Buat program Python yang memeriksa apakah suatu file sudah ada di direktori server. Jika file sudah
#             ada, program harus mencetak "File sudah ada," jika tidak, program harus mencetak "File belum
#             ada."
#             nama_file = "data.txt"
#             daftar_file_di_server = ["file1.txt", "file2.txt", "data.txt", "file3.txt"]

daftar_file_di_server = ['file1.txt', 'file2.txt', 'data.txt', 'file3.txt']
NAMA_FILE = 'data.txt'

if NAMA_FILE in daftar_file_di_server:
    print('File sudah ada')
else:
    print('File belum ada')
