print("\n OPERASI KONVERSI SUHU \n")

print("\n FAHRENHEIT \n ")

Fahrenheit = float(input("Masukan nilai suhu Fahrenheit : "))
print("Fahrenheit                          : ", Fahrenheit, "F")

Celsius = (Fahrenheit - 32) * (5/9)
print("Konversi Fahrenheit ke Celcius      : ", Celsius, "C")

Reamur = (4/9) * (Fahrenheit - 32)
print("Konversi Fahrenheit ke Reamur       : ", Reamur, "R")

Kelvin = (Fahrenheit + 459.67) * (5/9)
print("Konversi Fahrenheit ke Kelvin       : ", Kelvin, "K")
