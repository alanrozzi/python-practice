contadorProducto = 0
producto = ""
cantProducto = 0 #useless

#while True:
while producto != "salir":
    producto = input("Ingrese el nombre del producto o 'salir': ")

    if producto == 'salir':
        break

    cantProducto = int(input("Ingrese la cantidad del producto: "))

    contadorProducto =+ 1;


print("La cantidad total de productos es: ", contadorProducto)

