import types

def handle_mis_match(value):
    if not isinstance(value, (int, float)):
        raise TypeError("Value must be a number!")

handle_mis_match(4)  # Valid
# handle_mis_match("string")  # Uncomment untuk melihat error

# Fungsi: Menangani tipe data yang tidak sesuai.
# Kondisi: Ketika Anda ingin memberikan validasi tipe pada argumen.