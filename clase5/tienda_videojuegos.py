stockMaximo = 100
stockReponer = 20

stock = int(input("Ingrese la cantidad de stock a verificar: "))

if stock < stockReponer:
    print("Se necesita pedido urgente.")
else:
    if stock == 100:
        print("Stock maximo.")
    else:
        print("Se necesita stock.")

