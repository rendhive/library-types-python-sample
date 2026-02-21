import types

obj = [1, 2, 3]
print(type(obj))

if isinstance(obj, (types.ListType, list)):
    print("This is a list!")
# Fungsi: Menampilkan tipe objek dan memverifikasi menggunakan `types`.
# Kondisi: Ketika Anda ingin memeriksa tipe koleksi dalam kode.