def ejercicio_8():
    peso = float(input("Ingrese el peso de la mercancia: "))
    valor = float(input("Ingrese el valor de la mercancia: "))
    pago = input("Ingrese la forma de pago: ")

    if peso <= 500:
        tarifa = 40000
    elif 500 < peso <= 750:
        tarifa = 80000
    elif 750 < peso <= 1000:
        tarifa = 100000
    elif peso > 1000:
        tarifa = 500 * (peso // 10)

    if 300000 <= valor <= 600000:
        descuento = tarifa * 0.20
    elif 600000 < valor <= 1000000:
        descuento = tarifa * 0.35
    elif valor > 1000000:
        descuento = tarifa * 0.50

    if pago == "tarjeta":
        tarifa = 0
    elif pago == "efectivo" and valor > 500000:
        tarifa = 0
    elif 300000 < valor < 500000:
        descuento = tarifa * 0.50

    print("El valor es: ", tarifa - descuento)
ejercicio_8()