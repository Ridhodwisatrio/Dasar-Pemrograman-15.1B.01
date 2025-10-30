# Variable yang berulang menggunakan list/matriks
list_nim = []
list_uts = []
list_uas = []
list_total = []

ulang = 2
for i in range(ulang):
  print(f"\nData Ke- {str(i+1)}")
  list_nim.append(input("Masukan Nim anda: "))
  list_uts.append(int(input("Masukan Nilai UTS anda: ")))
  list_uas.append(int(input("Masukan Nilai UAS anda: ")))

# Proses
for i in range(ulang):
  list_total.append((list_uas[i]+list_uts[i])/2)

# Cetak
print(50*'=')
print("Nim         Nilai UTS         Nilai UAS       Total")
print(50*'=')
for i in range(ulang):
  print("%s\t%i\t\t%i\t\t%i"%(list_nim[i],list_uts[i],list_uas[i],list_total[i]))
print(50*'=')