data = [70,90,100,80,60]

item = 0

# iterasi
for nilai in data:
  item = item + nilai #sum / menjumlahkan seluruh data
  print(item)

# output jumlah semuanya
print(f"Jumlah Semuanya {item}")
print(f"Nilai rata-rata {item / len(data)}\n")

# range

print(list(range(10)))
# output: range(0,1,2,3,4,5,6,7,8,9)
print(list(range(2,8)))
# output: range(2,3,4,5,6,7)
print(list(range(2,20,3)))
# output: range(2,5,8,11,14,17)
print(list(range(3,15,3)),"\n")
# output: range(3,6,9,12)

# program untuk iterasi list menggunakan pengindeksan
mapel = ['matematika', 'fisika', 'kimia']

# iterasi list menggunakan indeks
for i in range(len(mapel)):
  print(f"Saya suka {mapel[i+1]}")