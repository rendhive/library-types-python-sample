import types

def debug_type(obj):
    if isinstance(obj, types.FunctionType):
        print(f"{obj.__name__} is a function.")
    elif isinstance(obj, types.ModuleType):
        print(f"{obj.__name__} is a module.")

debug_type(math)
debug_type(sample_function)
# Fungsi: Melakukan debugging dengan informasi tipe objek.
# Kondisi: Ketika Anda perlu mendapatkan informasi tentang tipe di saat runtime.