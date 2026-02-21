import types

def check_type(obj):
    if isinstance(obj, types.FunctionType):
        print("This is a function.")
    elif isinstance(obj, types.ModuleType):
        print("This is a module.")
    else:
        print("This is neither a function nor a module.")

check_type(math)  # Memeriksa module
check_type(sample_function)  # Memeriksa fungsi
# Fungsi: Memverifikasi dan memberikan logika berdasarkan tipe objek.
# Kondisi: Ketika Anda perlu melakukan pemeriksaan objek secara selektif.