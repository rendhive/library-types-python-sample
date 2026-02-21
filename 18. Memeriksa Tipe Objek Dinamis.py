import types

def check_type_dynamic(obj):
    type_name = type(obj).__name__
    if isinstance(obj, types.FunctionType):
        print(f"The object is a function of type {type_name}.")
    else:
        print(f"The object is of type {type_name}.")

check_type_dynamic(123)  # Integer
check_type_dynamic([])    # List
check_type_dynamic(lambda x: x)  # Lambda function
# Fungsi: Memeriksa dan memberikan informasi tentang tipe objek.
# Kondisi: Ketika Anda ingin merasa fleksibel dengan input objek.