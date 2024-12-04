#Hardcode
inventario = [
    ["manzanas", 3],
    ["queso rallado", 5]
]

print("Bienvenido :)")

while True:

    #MENU
    print("\n1. Agregar productos al inventario.")
    print("2. Mostrar productos disponibles en el inventario.")
    print("3. Salir")
    respuesta = input("\nEscriba del 1 al 3: ")

    #Verfica si se ingresa letra o numero.
    #49 = '1'
    #57 = '9'
    if (len(respuesta) == 1) and (ord(respuesta) > 48) and (ord(respuesta) < 58):
        respuesta = int(respuesta)

        #OPCIONES
        if respuesta == 1:

            #ALTA
            nombre = input("\nIngrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))

            inventario.append([nombre, cantidad])

        elif respuesta == 2:

            #MOSTRAR
            if len(inventario) == 0:
                print("\nNo existen productos en el inventario.")
            else:
                print("\nProductos disponibles:")
                #Recorre tanto filas como columnas al comportarse como matriz
                for i in range(0, (len(inventario))):
                    #for j in range(0, (len(inventario)-1)):
                        #print(f"- Producto: {inventario[i][j]} | Cantidad: {inventario[i][j+1]}")
                    print(f"- Producto: {inventario[i][0]} | Cantidad: {inventario[i][1]}")
        
        elif respuesta == 3:
            #SALIR
            print("\nGracias por usar nuestro sistema :)")
            break
        else:
            #OPCIONES NO VALIDAS
            print("\nEsa opcion esta fuera de nuestro rango :(")

    else:
        print("\nSolo aceptamos numeros ;)")