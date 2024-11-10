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
    respuesta = int(input("\nEscriba del 1 al 3: "))

    #OPCIONES
    if respuesta == 1:

        #ALTA
        nombre = input("\nIngrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad del producto: "))

        inventario.append([nombre, cantidad])

    elif respuesta == 2:

        #MOSTRAR
        if len(inventario) == 0:
            print("No existen productos en el inventario.")
        else:
            print("Productos disponibles:")
            for i in range(0, (len(inventario))):
                print(inventario[i])
    
    elif respuesta == 3:
        #SALIR
        print("\nGracias por usar nuestro sistema :)")
        break
    else:
        #OPCIONES NO VALIDAS
        print("\nEsa opcion esta fuera de nuestro rango :(")