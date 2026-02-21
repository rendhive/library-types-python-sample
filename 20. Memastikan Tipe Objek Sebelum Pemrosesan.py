import types

def ensure_function(func):
    if not isinstance(func, types.FunctionType):
        raise ValueError("Provided argument is not a function.")
    print(f"{func.__name__} is a valid function.")

ensure_function(sample_function)  # Valid
# ensure_function(123)  # Uncomment untuk melihat error
# Fungsi: Memastikan argumen yang diterima adalah fungsi sebelum menjalankannya.
# Kondisi: Ketika Anda ingin mengimplementasikan validasi yang lebih ketat