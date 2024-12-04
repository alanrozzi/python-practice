# Tu programa debe permitir al usuario consultar el inventario de una tienda
# para verificar si un producto está en stock.
# Si el producto está en la lista, el programa debe informarlo,
# si no, debe mostrar un mensaje indicando que no está disponible.





# Usá una lista para almacenar los productos en stock.
#Hardcode
inventario = [
    "manzanas",
    "queso rallado"
]

while True:

    #MENU
    print("\n1. Consultar productos del inventario.")
    print("2. Mostrar productos disponibles en el inventario.")
    print("3. Salir")
    respuesta = int(input("\nEscriba del 1 al 3: "))

    #OPCIONES
    if respuesta == 1:

        i=0;

        #CONSULTA
        # Permití que el usuario ingrese el nombre de un producto a consultar.
        nombre = input("Ingrese el nombre del producto: ")

        # Recorré la lista con un bucle while para verificar si el producto está en stock.
        while i < len(inventario):
            if inventario[i] == nombre:
                print(f"\n{nombre}, existe en este inventario.")
                break;
            i+=1

        if i == len(inventario):
            print("\nNo existen el producto indicado.")
        

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