n = [1,2,3,4]

# nambah satu data (.append)
n.append(5)
print(n)

# nambah banyak data (.extend)
n.extend([6,7,8,9,10])
print(n)

# ubah data (var [index]  = value)
n [0] = 100
print(n)

# hapus data by value(.remove)
n.remove(2)
print(n)

# hapus data by index (.pop)
n.pop(1)
print(n)

# menyisipkan  data
n1 = [1,2,3,4]
n1.insert(1,5)
print(n1)

# Mengurutkan list
alfabet = ['a','b','d','f','e','c','h','g','j','i']

# alfabet.sort()
# print(alfabet)

print("Urut ascending: ",sorted(alfabet))

print("Urut descending: ",sorted(alfabet,reverse=True))