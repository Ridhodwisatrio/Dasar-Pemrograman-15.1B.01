# Layar Masukan
print("GEROBAK FRIED CHICKEN")
print(35*"-")
print("Kode\t","Jenis potong\t","Harga")
print(35*"-")
print("D\t", "Dada\t", "\tRp. 2500")
print("P\t", "Paha\t", "\tRp. 2000")
print("S\t", "Sayap\t", "\tRp. 1500")
print(35*"-","\n")

# input
banyak_jenis = int(input("Banyak jenis: "))
for i in range(banyak_jenis):
  print(f"Jenis ke- {str(i+1)}")
  kode_potong = input("Masukan kode potong [D/P/S]: ")
  banyak_potong = int(input("Masukan banyak potong: "))
b = 0

# proses if
if kode_potong.upper() == "D":
  jenis_potong = "Dada"
  harga = 2500
elif kode_potong.upper() == "P":
  jenis_potong = "Paha"
  harga = 2000
elif kode_potong.upper() == "S":
  jenis_potong = "Sayap"
  harga = 1500
else:
  jenis_potong = "Maaf jenis potong tidak tersedia"
  harga = 0
jenis_jenis = ['Dada', 'Paha', 'Sayap']
# output
print("\tGEROBAK FRIED CHICKEN")
print(35*"-")
print('''NO. Jenis\t Harga\t Banyak\t Jumlah
    Potong\t Satuan\t Beli\t Harga''')
print(35*"-")
for i in range(len(jenis_jenis)):
  print(b,".",jenis_jenis[i],"\t", harga,"\t", banyak_potong,"\t", "Rp.", (banyak_potong * harga))
print(35*"-")
print(f"Jumlah Bayar: Rp.{harga + harga}" )
print(f"Pajak 10%: Rp.{harga * 0.1}")






