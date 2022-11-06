print("\n OPERASI KONVERSI SUHU \n")

print("\n REAMUR \n ")

Reamur = float(input("Masukan nilai suhu Reamur : "))
print("Reamur                          : ", Reamur, "R")

Celsius = Reamur / 0.8
print("Konversi Reamur ke Celcius      : ", Celsius, "C")

Fahrenheit = (Reamur * 2.25) + 32
print("Konversi Reamur ke Fahrenheit   : ", Fahrenheit, "F")

Kelvin = (Reamur / 0.8) + 273.15
print("Konversi Reamur ke Kelvin       : ", Kelvin, "K")
