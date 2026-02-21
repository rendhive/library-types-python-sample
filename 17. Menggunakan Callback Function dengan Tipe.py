import types

def callback_function(f: types.FunctionType) -> None:
    f()

def display_message():
    print("This is a callback!")

callback_function(display_message)  # Fungsi callback
# Fungsi: Menggunakan dan menerima fungsi callback dengan tipe yang jelas.
# Kondisi: Ketika Anda ingin mendefinisikan fungsi penghubung atau callback.