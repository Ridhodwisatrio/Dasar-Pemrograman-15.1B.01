# input
gaji_pokok = 300000
print("PROGRAM HITUNG GAJI KARYAWAN")
nama = input("Nama Karyawan: ")
jabatan = int(input("Golongan Jabatan [1/2/3]: "))
pendidikan = input("Pendidikan [SMA/D1/D3/S1]: ")
jam_kerja = int(input("Jumlah Jam Kerja: "))

# proses tunjangan jabatan
if jabatan == 3:
  tunjangan_jabatan = gaji_pokok * 0.15
elif jabatan == 2:
  tunjangan_jabatan = gaji_pokok * 0.1
else:
  tunjangan_jabatan = gaji_pokok * 0.05

# proses tunjangan pendidikan
if pendidikan.upper() == "S1":
  tunjangan_pendidikan = gaji_pokok * 0.3
elif pendidikan.upper() == "D3":
  tunjangan_pendidikan = gaji_pokok * 0.2
elif pendidikan.upper() == "D1":
  tunjangan_pendidikan = gaji_pokok * 0.05
else:
  tunjangan_pendidikan = gaji_pokok * 0.025

# proses lembur
if jam_kerja > 8:
  honor_lembur = (jam_kerja - 8) * 3500
total_gaji = gaji_pokok + tunjangan_jabatan + tunjangan_pendidikan +honor_lembur

# output
print('==================================')
print("Karyawan atas nama: ",nama)
print("Honor yang diterima")
print("   Tunjangan jabatan: Rp.",str(tunjangan_jabatan))
print("   Tunjangan pendidikan: Rp.",str(tunjangan_pendidikan))
print("   Honor lembur: Rp.",str(honor_lembur))
print("   Total gaji: Rp.",str(total_gaji))
