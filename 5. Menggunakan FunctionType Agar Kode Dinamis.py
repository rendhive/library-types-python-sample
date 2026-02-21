import types

def outer_function():
    def inner_function():
        return "Inner function"

    return inner_function

func = outer_function()
print(isinstance(func, types.FunctionType))  # Memeriksa apakah ini adalah fungsi
# Fungsi: Menggunakan FunctionType untuk menangani fungsi yang dihasilkan oleh fungsi lain.
# Kondisi: Ketika Anda ingin berinteraksi dengan closure dan fungsi dinamis.