import types

new_function = types.FunctionType(
    compile("return 'Hello, World!'", "<string>", "eval"),
    {}
)

print(new_function())  # Memanggil fungsi yang dibuat secara dinamis
# Fungsi: Membuat dan menjalankan fungsi baru secara dinamis menggunakan jenis fungsi.
# Kondisi: Ketika Anda ingin membuat fungsi pada run-time berdasarkan string.