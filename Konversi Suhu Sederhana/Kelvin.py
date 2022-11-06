print("\n OPERASI KONVERSI SUHU \n")

print("\n KELVIN \n ")

Kelvin = float(input("Masukan nilai suhu Kelvin : "))
print("Kelvin                          : ", Kelvin,    "K")

Celsius = Kelvin - 273.15
print("Konversi Kelvin ke Celcius      : ", Celsius,    "C")

Fahrenheit = (Kelvin * (9/5)) - 459.67
print("Konversi Kelvin ke Fahrenheit   : ", Fahrenheit, "F")

Reamur = (4/5) * (Kelvin - 273)
print("Konversi Kelvin ke Reamur       : ", Reamur,     "R")
