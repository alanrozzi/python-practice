from validaciones import  buscarProducto

def hardcodeProductos():
    
    inventario = {
        1: {"nombre": "Test1",
            "descripcion": "TestDesc1",
            "cantidad": 0,
            "precio": 0.0,
            "categoria": "TestCat"},

        2: {"nombre": "Test2",
            "descripcion": "TestDesc2",
            "cantidad": 0,
            "precio": 0.0,
            "categoria": "TestCat"},

        3: {"nombre": "Test3",
            "descripcion": "TestDesc3",
            "cantidad": 0,
            "precio": 0.0,
            "categoria": "TestCat"},

        4: {"nombre": "Test4",
            "descripcion": "TestDesc4",
            "cantidad": 0,
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
    inventario[key]["cantidad"] = int(input("Ingrese la cantidad del producto: "))
    inventario[key]["precio"] = float(input("Ingrese el precio del producto: "))
    inventario[key]["categoria"] = input("Ingrese la categoria del producto: ")

    #print(inventario[len(inventario)])
    return inventario
   
def mostrarProductos(inventario, mensajeEliminados):

    if len(inventario) == 0:
        print(f"\nNo existen productos{mensajeEliminados} en el inventario.")
    else:
        print(f"\nInventario de productos{mensajeEliminados}:")
        for key, producto in inventario.items():
            print(f"\nProducto: {key}"
                f"\n\tNombre: {producto["nombre"]}"
                f"\n\tDescripcion: {producto["descripcion"]}"
                f"\n\tCantidad: {producto["cantidad"]}"
                f"\n\tPrecio: {producto["precio"]}"
                f"\n\tCategoria: {producto["categoria"]}")
    

# Esta función debería solicitar que se ingrese el código del
# producto a actualizar, y verificar si existe en nuestro
# diccionario. En caso afirmativo se piden el o los datos a
# actualizar y se efectúa el reemplazo de los valores en el
# diccionario. Si el producto cuyo código hemos ingresado no 
# existe, se puede mostrar un mensaje explicando la
# situación antes de salir de la función.

def actualizarProducto(inventario):

    print(f"\nCantidad de productos disponibles: {len(inventario)}")
    if len(inventario) == 0:
        print("No se puede actualizar el inventario.")
    else:
        codigo = buscarProducto(inventario)
        if codigo != -1:
            #Completo campos del inventario
            inventario[codigo]["nombre"] = input("Ingrese el nuevo nombre del producto: ")
            inventario[codigo]["descripcion"] = input("Ingrese la nueva descripcion del producto: ")
            inventario[codigo]["cantidad"] = int(input("Ingrese la nueva cantidad del producto: "))
            inventario[codigo]["precio"] = float(input("Ingrese el nuevo precio del producto: "))
            inventario[codigo]["categoria"] = input("Ingrese la nueva categoria del producto: ")


# debe pedir el código del producto a borrar, buscarlo en el diccionario, y si lo encuentra,
# quitarlo de él. Si no lo encuentra, podemos notificar a la usuaria o usuario de esta situación.

def eliminarProducto(inventario, inventarioEliminado):
    print(f"\nCantidad de productos disponibles: {len(inventario)}")
    if len(inventario) == 0:
        print("No se puede eliminar productos del inventario.")
    else:
        codigo = buscarProducto(inventario)
        if codigo != -1:
            #Elimino el producto
            print("Agregado en papelera.")
            inventarioEliminado[codigo] = inventario.pop(codigo, "No se pudo eliminar")