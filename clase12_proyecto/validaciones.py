def menu():
    print("\n1. Agregar producto al inventario.")
    print("2. Mostrar productos disponibles en el inventario.")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Ver productos eliminados")
    print("6. Buscar producto")
    print("7. Buscar productos de bajo stock")
    print("8. Salir")
    print("\n9. (Dev only) Hardcode.")

def validarRespuesta(respuesta, letraMin, letraMax):

    #Verfica si se ingresa letra o numero.
    #49 = '1'
    #57 = '9'
    validacion = False
    if(len(respuesta) == 1) and (ord(respuesta) >= letraMin) and (ord(respuesta) <= letraMax):
        validacion = True

    return validacion

def validarNumero(mensaje, tipo):
    codigoValido = 0
    while True:
        codigoValido = input(mensaje)
        if codigoValido.isdigit() and (int(codigoValido) > 0 or float(codigoValido) > 0):
            
            if tipo == "int":
                codigoValido = int(codigoValido)
                break
            if tipo == "float":
                codigoValido = float(codigoValido)
                break

    return codigoValido

def codigoProducto(inventario):

    if len(inventario) == 0:
        print("No existen productos del inventario.")
    else:
        codigo = validarNumero("Ingrese un codigo valido de producto: ", "int")
        if codigo > len(inventario):
            print(f"\nEl producto {codigo} no existe en este inventario.")
            codigo = -1
        else:
            print(f"\nCodigo: {codigo}.")

    return codigo

    

