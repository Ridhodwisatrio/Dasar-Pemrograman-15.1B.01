# inpuut
nama = input("Masukan nama: ")
nis = input("Masukan nis: ")
jurusan = input("Masukan jurusan [SI/SIA]: ")

# proses
if jurusan.upper() == "SI":
  nama_prodi = "Sistem Informasi"
  biaya = 2400000
elif jurusan.upper() == "SIA":
  nama_prodi = "Sistem Informasi Akuntansi"
  biaya = 2000000
else:
  nama_prodi = "Nama prodi tidak ada"
  biaya = 0

# output
print("\n" + 5*"=" + "Pendaftaran Mahasiswa Baru" + 5*"=")
print(f"Nama   :{nama}")
print(f"Nis    :{nis}")
print(f"Jurusan:{nama_prodi.upper()}")
print(f"Biaya  :{biaya}")
print(37*"=")