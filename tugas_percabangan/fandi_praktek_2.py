# Nama      : Moh. Dwi Afandi
# Absen     : 18
# Kelas     : XI TKJ 2
# Soal      : Buat program Python yang mengambil estimasi waktu selesai proyek dan tanggal target selesai. Jika
#             estimasi waktu selesai lebih awal atau sama dengan tanggal target, program harus mencetak "Tepat
#             waktu," jika tidak, program harus mencetak "Terlambat."


estimasi_waktu = float(input('Estimasi waktu selesai proyek : '))
tanggal_target = float(input("Tanggal Target selesai : "))

if tanggal_target <= estimasi_waktu:
    print('Target tepat waktu')

else:
    print("Terlambat")
    