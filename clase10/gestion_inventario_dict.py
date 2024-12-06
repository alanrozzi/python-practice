# En un comercio, se necesita gestionar los productos y sus precios. Desarrollá un programa que permita:
# 1
# Ingresar el nombre de tres productos y su precio correspondiente, guardándolos en un diccionario donde
# la clave es el nombre del producto y el valor es su precio.
# 2
# Una vez ingresados, mostrará todos los productos y sus precios en pantalla.

# Producto: Manzanas, Precio: 100
# Producto: Naranjas, Precio: 150
# Producto: Peras, Precio: 120

productos = {"Manzanas": 50,
             "Peras": 30,
             "Bananas": 40
            }

for i in range(1, 4):
    claveProducto = input(f"Ingrese el nombre del producto {i}: ")
    valorProducto = int(input(f"Ingrese la cantidad del producto {i}: "))

    productos[claveProducto] = valorProducto

for producto, cantidad in productos.items():
    print(f"Producto: {producto}, cantidad: {cantidad}")