
# Te permita ingresar el nombre de un producto.

# Utilice el método .get() para buscar el stock disponible. Si el producto no existe, deberá mostrar un
# mensaje diciendo "Producto no encontrado".

# Si el producto está disponible, mostrará cuántas unidades quedan en stock.

productos = {
    "Manzanas": 50,
    "Naranjas": 30,
    "Peras": 25
}

nombreProducto = input(f"Ingresá el nombre del producto: ")

if productos.get(nombreProducto, "NONE") != "NONE":
    print(f"Stock disponible de {nombreProducto}: {productos.get(nombreProducto, "NONE")}")
else:
    print("Producto no encontrado")