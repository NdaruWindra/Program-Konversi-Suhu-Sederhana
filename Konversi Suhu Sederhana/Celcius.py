print("\n OPERASI KONVERSI SUHU \n")

print("\n CELCIUS \n ")

Celcius = float(input("Masukan nilai suhu Celcius : "))
print("Celcius                        : ", Celcius, "C")

Reamur = ((5/4) * Celcius)
print("Konversi Celcius ke Reamur     : ", Reamur, "R")

Fahrenheit = ((9/5) * Celcius) + 32
print("Konversi Celcius ke Fahrenheit : ", Fahrenheit, "F")

Kelvin = Celcius + 273
print("Konversi Celcius ke Kelvin     : ", Kelvin, "K")
