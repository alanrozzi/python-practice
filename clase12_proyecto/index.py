#Como importar funcionesd desde otro archivo:

#Como fichero:
#import 'nombre_archivo.py' (donde se encuentran las funciones)
#Uso:
#nombre_archivo.funcion

#from 'nombre_archivo.py' (fichero) import 'funcion1', 'funcion2'

from validaciones import validarRespuesta, menu
from funciones import hardcodeProductos, resgistrarProducto, mostrarProductos, actualizarProducto, eliminarProducto, buscarProducto, reportarBajoStock


inventario = {}
inventarioEliminado = {}

print("Bienvenido :)")

while True:

    #MENU
    menu()
    respuesta = input("\nEscriba del 1 al 8: ")

    #Verfica si se ingresa letra o numero.
    #49 = '1'
    #57 = '9'
    if (validarRespuesta(respuesta, 49, 57)):
        respuesta = int(respuesta)

        #OPCIONES
        if respuesta == 1:

            #ALTA
            resgistrarProducto(inventario)
            #DEBUG
            #print(inventario)

        elif respuesta == 2:

            #MOSTRAR
            mostrarProductos(inventario, "")
        
        elif respuesta == 3:
            #ACTUALIZAR
            actualizarProducto(inventario)

        elif respuesta == 4:
            #ELIMINAR
            eliminarProducto(inventario, inventarioEliminado)

        elif respuesta == 5:
            #ACTUALIZAR
            mostrarProductos(inventarioEliminado, " eliminados")

        elif respuesta == 6:
            #BUSCAR
            buscarProducto(inventario)

        elif respuesta == 7:
            #BUSCAR
            reportarBajoStock(inventario, 5)

        elif respuesta == 8:
            #SALIR
            print("\nGracias por usar nuestro sistema :)")
            break

        elif respuesta == 9:
            #HARDCODE
            inventario = hardcodeProductos()
            print("\nHardcode finalizado")

        else:
            #OPCIONES NO VALIDAS
            print("\nEsa opcion esta fuera de nuestro rango :(")

    else:
        print("\nSolo aceptamos numeros ;)")