# Menggunakan kutip tiga
print('''He said, "What's there?"''')
# Menggunakan karakter escape untuk tanda kutip tunggal
print('He said, "What\'s there?"')
# Menggunakan karakter escape untuk tanda kutip ganda
print("He said, \"What's there?\"")
print('Ini adalah \x48\x45\x58')
print("This is \x61 \ngood example")
print(r"This is \x61 \ngood example")

# Menggunakan posisi default
default_order = "{}, {} dan {}".format("Budi", "Galih", "Ratna", "Lil")
print('\n--- Urutan Default ---')
print(default_order)

# Menggunakan argument posisi 
positional_order = "{1}, {0}, {2} dan {2}".format("Budi", "Galih", "Ratna", "Lil")
print('\n--- Urutan berdasarkan posisi ---')
print(positional_order)

# format integer
print("{0} bila diubah jadi biner menjadi {0:b}".format(12))
# format eksponensial
print("Format eksponensial: {0:e}".format(1566.345))
# format pembulatan
print("Sepertiga = {0:3f}".format(1/3))
# meratakan string
print("|{:<10}|{:^10}|{:>10}".format('beras', 'gula', 'garam'))
print('\n')

print("Universitas Bina Sarana Informatika".lower())
print("Universitas Bina Sarana Informatika".upper())
print("I Love Programming in Python".split())
print("I Love Python".startswith("I"))
print("Saya Belajar Python".endswith("on"))
print(' - '.join(['I', 'Love', 'You']))
print("Belajar Java di BSI".replace('Java', 'Python'))