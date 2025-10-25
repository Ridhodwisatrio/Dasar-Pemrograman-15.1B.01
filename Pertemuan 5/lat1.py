ulang = int(input("Masukan angka berapapun yang kamu mau: "))
for i in range(ulang):
  print(f"Data ke- {str(i+1)}")
  nama = input("Masukan Nim anda: ")
  uts =int(input("Masukan nilai UTS anda: "))
  uas =int(input("Masukan nilai UAS anda: "))
  print("Nim anda adalah %s nilai UTS anda %i nilai UTS anda %i" % (nama,uts,uas))
  print(20*"-")