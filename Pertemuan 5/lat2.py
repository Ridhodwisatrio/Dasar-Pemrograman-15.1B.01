# Layar Masukan
print(''' \nGEROBAK FRIED CHICKEN
--------------------------------
Kode  Jenis Potong  Harga
D     Dada          Rp.2500
P     Paha          Rp.2000
S     Sayap         Rp.1500
--------------------------------
''')

# inisialisai data list
jenis_potong = []
harga_satuan = []
banyak_beli = []
total_semua = []

# input
banyak_jenis = int(input("Banyak jenis: "))
for i in range(banyak_jenis):
  print(f"\nJenis ke- {str(i+1)}")
  kode_potong = input("Masukan kode potong [D/P/S]: ")
  banyak_potong = int(input("Masukan banyak potong: "))
  if kode_potong.upper() == "D":
    jenis = "Dada"
    harga = 2500
  elif kode_potong.upper() == "P":
    jenis = "Paha"
    harga = 2000
  elif kode_potong.upper() == "S":
    jenis = "Sayap"
    harga = 1500
  else:
    jenis = "Maaf jenis potong tidak tersedia"
    harga = 0
  total = harga * banyak_potong
# tempat buat nyimpen list
  jenis_potong.append(jenis)
  harga_satuan.append(harga)
  banyak_beli.append(banyak_potong)
  total_semua.append(total)

# output
print('''\nGEROBAK FRIED CHICKEN
-----------------------------------------
No. Jenis     Harga     Banyak     Jumlah
    Potong    Satuan    Beli       Harga
-----------------------------------------
''')
jumlah_harga = 0
for i in range(banyak_jenis):
  print(i+1,".",jenis_potong[i],"    ",harga_satuan[i],"\t", banyak_beli[i],"\t", "  Rp.",total_semua[i])
  jumlah_harga += total_semua[i]
pajak = jumlah_harga * 0.1
print(41*"-")
print(f"Jumlah Bayar: Rp.{jumlah_harga}" )
print(f"Pajak 10%: Rp.{pajak}")
print(f"Total Bayar: Rp.{jumlah_harga + pajak}")






