# input
pembeli = input("Masukan Nama Pembeli: ")
no_hp = input("Masukan No. Handphone: ")
jurusan = input("Masukan Jurusan [SBY/BL/LMP]: ")
jumlah = int(input("Masukan Jumlah Beli: "))

# proses
if jurusan.upper() == "SBY":
  nama_jurusan = "Surabaya"
  harga = 300000
elif jurusan.upper() == "BL":
  nama_jurusan = "Bali"
  harga = 350000
else :
  nama_jurusan = "Lampung"
  harga = 500000

# proses potongan
if jumlah >= 3:
  potongan = (jumlah * harga) * 0.1
else:
  potongan = 0
total = (jumlah * harga) - potongan

# output
print("-----------------------------------------")
print("          PENJUALAN TIKET BUS")
print("                XYZ")
print("Nama Pembeli :"+str(pembeli))
print("No. Handphone :"+str(no_hp))
print("Kode Jurusan Yang Dipilih :"+str(jurusan.upper()))
print("Nama Kota Tujuan :"+str(nama_jurusan))
print("Harga :"+str(harga))
print("Jumlah beli :"+str(jumlah))
print("------------------------------------------")
print("Potongan Yang Didapat :"+str(potongan))
print("Total Bayar :"+str(total))
ubay = int(input("Masukan Uang Bayar: "))
uang_kembali = ubay-total
print("Uang Kembali :"+str(uang_kembali))