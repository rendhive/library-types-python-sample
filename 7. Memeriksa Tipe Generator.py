import types

def generator_function():
    yield 1

gen = generator_function()
print(isinstance(gen, types.GeneratorType))  # Memeriksa apakah ini adalah generator
# Fungsi: Memeriksa apakah objek adalah generator.
# Kondisi: Ketika Anda ingin memastikan objek adalah generator untuk operasi lebih lanjut.