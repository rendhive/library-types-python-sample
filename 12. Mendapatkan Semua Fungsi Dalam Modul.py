import types
import math

# Mendapatkan semua fungsi dalam modul
functions = [func for func in dir(math) if isinstance(getattr(math, func), types.FunctionType)]
print(functions)
# Fungsi: Mengambil semua fungsi yang ada dalam modul math.
# Kondisi: Ketika Anda ingin mengeksplorasi fungsi dalam sebuah modul.