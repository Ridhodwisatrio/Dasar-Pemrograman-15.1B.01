nilai = int(input("Masukan Nilai: "))
if nilai >= 80 and nilai <= 100:
  grade = "A"
elif nilai >= 70 and nilai <= 79:
  grade = "B"
elif nilai >= 60 and nilai <= 69:
  grade = "C"
elif nilai >= 31 and nilai <= 59:
  grade = "D"
else:
  grade = "E"

print("Nilai anda:",nilai)
print("Predikat:",grade)