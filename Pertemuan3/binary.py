# binary
print(bin(1))
print(bin(7))

print("====Is====")
# identity
# is
a = 10
b = 5
c = a > b
if c is True:
  print("Nilai a lebih besar dari nilai b ")
else:
  print("Nilai a tidak lebih besar dari nilai b ")

print("===========Is not===========")
# is not
a = 10
b = 5
c = a > b
if c is not True:
  print("Nilai a lebih besar dari nilai b ")
else:
  print("Nilai a tidak lebih besar dari nilai b ")

print("==========In============")
# operator keanggotaan
a = [5, 10, 1, 20, 100]
if 11 in a:
  print("11 ada di dalam a")
else:
  print("11 tidak ada di dalam a")
