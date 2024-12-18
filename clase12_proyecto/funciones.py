from validaciones import  codigoProducto, validarNumero

def hardcodeProductos():
    
    inventario = {
        1: {"nombre": "Test1",
            "descripcion": "TestDesc1",
            "cantidad": 0,
            "precio": 0.0,
            "categoria": "TestCat"},

        2: {"nombre": "Test2",
            "descripcion": "TestDesc2",
            "cantidad": 3,
            "precio": 0.0,
            "categoria": "TestCat"},

        3: {"nombre": "Test3",
            "descripcion": "TestDesc3",
            "cantidad": 6,
            "precio": 0.0,
            "categoria": "TestCat"},

        4: {"nombre": "Test4",
            "descripcion": "TestDesc4",
            "cantidad": 9,
            "precio": 0.0,
            "categoria": "TestCat"}

    }

    return inventario

# Agregar los productos en el diccionario inventario con un código único y sus respectivos datos.
def resgistrarProducto(inventario):
    #Pedido de datos a agregar
    #Creo key siguiente de la cantidad de productos existentes
    key = len(inventario)+1
    #Creo nueva instancia del inventario
    inventario[key] = {}
    #Completo campos del inventario
    inventario[key]["nombre"] = input("Ingrese el nombre del producto: ")
    inventario[key]["descripcion"] = input("Ingrese la descripcion del producto: ")
    #VALIDAR SOLO INT y FLOAT
    inventario[key]["cantidad"] = validarNumero("Ingrese la cantidad valida del producto: ", "int")
    #SOLO ADMITE INTS
    inventario[key]["precio"] = validarNumero("Ingrese el precio valido del producto: ", "float")

    inventario[key]["categoria"] = input("Ingrese la categoria del producto: ")

    #print(inventario[len(inventario)])
    return inventario
   
#Muestra la lista completa del inventario
def mostrarProductos(inventario, mensaje):

    if len(inventario) == 0:
        print(f"\nNo existen productos{mensaje} en el inventario.")
    else:
        print(f"\nInventario de productos{mensaje}:")
        for key, producto in inventario.items():
            print(f"\nProducto: {key}"
                f"\n\tNombre: {producto["nombre"]}"
                f"\n\tDescripcion: {producto["descripcion"]}"
                f"\n\tCantidad: {producto["cantidad"]}"
                f"\n\tPrecio: {producto["precio"]}"
                f"\n\tCategoria: {producto["categoria"]}")
            
#Muestra solo un producto de la lista mediante su key
def mostrarProducto(inventario, key):

    print(f"\nProducto: {key}"
        f"\n\tNombre: {inventario[key]["nombre"]}"
        f"\n\tDescripcion: {inventario[key]["descripcion"]}"
        f"\n\tCantidad: {inventario[key]["cantidad"]}"
        f"\n\tPrecio: {inventario[key]["precio"]}"
        f"\n\tCategoria: {inventario[key]["categoria"]}")
    
#Actualiza un producto del inventario mediante su key
def actualizarProducto(inventario):

    print(f"\nCantidad de productos disponibles: {len(inventario)}")
    if len(inventario) == 0:
        print("No se puede actualizar el inventario.")
    else:
        key = buscarProducto(inventario)
        if key != -1:
            #Completo campos del inventario
            inventario[key]["nombre"] = input("Ingrese el nuevo nombre del producto: ")
            inventario[key]["descripcion"] = input("Ingrese la nueva descripcion del producto: ")
            inventario[key]["cantidad"] = validarNumero("Ingrese la nueva cantidad valida del producto: ", "int")
            inventario[key]["precio"] = validarNumero("Ingrese el nuevo precio valido del producto: ", "float")

            inventario[key]["categoria"] = input("Ingrese la nueva categoria del producto: ")



def eliminarProducto(inventario, inventarioEliminado):
    print(f"\nCantidad de productos disponibles: {len(inventario)}")
    if len(inventario) == 0:
        print("No se puede eliminar productos del inventario.")
    else:
        key = codigoProducto(inventario)
        if key != -1:
            #Elimino el producto
            print("Agregado en papelera.")
            inventarioEliminado[key] = inventario.pop(key, "No se pudo eliminar")

def buscarProducto(inventario):
    key = codigoProducto(inventario)
    #if key in inventario:
    if key != -1:
        #Busco el producto
        mostrarProducto(inventario, key)


def reportarBajoStock(inventario, bajoStock):
    
    if len(inventario) == 0:
        print("No existen productos del inventario.")
    else:
        inventarioBajoStock = {}

        for key, producto in inventario.items():
            if producto["cantidad"] <= bajoStock:
                inventarioBajoStock[key] = inventario[key]

        mostrarProductos(inventarioBajoStock, " de bajo stock (5 o menos)")