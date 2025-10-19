# input
nama_barang = input("Masukan Nama Barang :")
harga_barang = int(input("Masukan harga barang :"))
jumlah_barang = float(input("Masukan jumlah barang :"))
# proses
total_bayar = harga_barang * jumlah_barang
# output
print("Nama barang :", nama_barang)
print("Harga yang harus dibayar :Rp.",total_bayar, "\n")

print("===Input===")
print("=+=+=+ Data Diri Mahasiswa =+=+=+")
nim = input("NIM :")
nama = input("Nama Lengkap :")
jurusan = input("Jurusan :")
alamat = input("Alamat :")
print("====Output====")
print("Hasil cetak data di atas adalah")
print("Nim :" +str(nim))
print("Nama : " +str(nama))
print("Jurursan :" +str(jurusan))
print("Alamat :" +str(alamat))