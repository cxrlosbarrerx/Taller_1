#Elaborar un programa que pida a dos usuarios el nombre y la edad e imprima el nombre del menor.
nombre_1 = input("ingrese su nombre: ")
edad_1 = int(input("ingrese su edad: "))

nombre_2 = input("ingrese su nombre")
edad_2 = int(input("ingrese su edad"))
if edad_1 < edad_2:
    menor = nombre_1
else:
    menor = nombre_2

print("nombre del menor:", menor)