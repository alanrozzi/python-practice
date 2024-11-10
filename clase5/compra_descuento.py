montoTotal = float(input("Ingrese el monto total de compra: "))
cantArticulos = int(input("Ingrese la cantidad de articulos: "))

if montoTotal > 10000:
    if cantArticulos >= 5:
        montoTotal*=0.85
else:
    if (cantArticulos < 5) and (cantArticulos > 3):
        montoTotal*=0.90


print("El monto total es de:", montoTotal)