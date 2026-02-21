import types

def decorator_function(func):
    def wrapper():
        print("Function is being called...")
        return func()
    return wrapper

@decorator_function
def my_function():
    return "Hello!"

print(my_function())  # Menggunakan decorator pada fungsi
# Fungsi: Menunjukkan penggunaan decorator dalam konteks fungsi.
# Kondisi: Ketika Anda ingin mengubah perilaku fungsi dengan decorator.