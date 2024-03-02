#Desarrollar un algoritmo para leer la temperatura en grados centígrados y muestre su resultado en Fahrenheit y kelvin.
Celcius = float(input("ingresar temperatura: "))

Fahrenheit = (Celcius * 9/5) + 32
Kelvin = Celcius + 273.15

print("En Fahrenheit son: ", Fahrenheit)
print("En Kelvin son: ", Kelvin)
