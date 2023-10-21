# Nama      : Moh. Dwi Afandi
# Absen     : 18
# Kelas     : XI TKJ 2
# Soal      : Buat program Python yang mengambil nilai tugas (skala 0-100) dan nilai ujian (skala 0-100) seorang
#             siswa dan menentukan nilai akhirnya. Jika nilai tugas lebih dari 70 dan nilai ujian lebih dari 60, siswa
#             lulus dengan nilai "Lulus". Jika tidak, siswa gagal dengan nilai "Gagal".


def main() -> str:
    '''
    Program Python 
    --------------
    '''
    nilai_tugas = float(input("Masukkan nilai tugas: "))
    nilai_ujian = float(input("Masukkan nilai ujian: "))

    assert 0 <= nilai_tugas <= 100, "Nilai Tugas harus berada di rentang (0 - 100)"
    assert 0 <= nilai_ujian <= 100, "Nilai Ujian harus berada di rentang (0 - 100)"

    if nilai_tugas > 70 and nilai_ujian > 60:
        return 'Siswa Lulus'
    else:
        return 'Siswa Gagal'
    
if __name__ == "__main__":
    print(main())
