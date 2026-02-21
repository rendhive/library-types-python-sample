import types

class Example:
    def method_one(self):
        pass

    def method_two(self):
        pass

all_members = [member for member in dir(Example) if isinstance(getattr(Example, member), types.FunctionType)]
print(all_members)
# Fungsi: Mengambil semua metode dalam kelas.
# Kondisi: Ketika Anda ingin mengecek semua metode dalam kelas yang sudah didefinisikan.