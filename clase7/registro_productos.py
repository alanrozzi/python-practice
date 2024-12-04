# Vas a implementar un sistema básico para registrar productos en el inventario de una tienda.
# El programa debe permitir que el usuario agregue productos a una lista hasta que decida no agregar más.
# Luego, deberás mostrar todos los productos ingresados al inventario.

#Hardcode
inventario = [
    "manzanas",
    "queso rallado"
]

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
        inventario.append(nombre)

    elif respuesta == 2:

        #MOSTRAR
        if len(inventario) == 0:
            print("\nNo existen productos en el inventario.")
        else:
            print("\nProductos disponibles:")
            #Recorre tanto filas como columnas al comportarse como matriz
            for prod in inventario:
                print(f"- Producto: {prod}")

    elif respuesta == 3:
        #SALIR
        print("\nGracias por usar nuestro sistema :)")
        break
    else:
        #OPCIONES NO VALIDAS
        print("\nEsa opcion esta fuera de nuestro rango :(")