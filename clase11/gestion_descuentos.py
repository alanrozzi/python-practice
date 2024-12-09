# Imaginá que en tu tienda querés implementar un sistema de descuentos automáticos.
# Vas a desarrollar un programa que permita
# calcular el precio final de un producto después de aplicar un descuento. Para hacerlo:

# Crea una función que reciba como parámetros el precio original del producto
# y el porcentaje de descuento, y que retorne
# el precio final con el descuento aplicado.

# Luego, pedí que se ingrese el precio y el porcentaje de descuento.
# Mostrá el precio final después de aplicar el descuento.

def aplicarDescuento(precioOriginal, porcentajeDescuento):
    return precioOriginal - (precioOriginal*(porcentajeDescuento/100))

precio = float(input("Ingrese el precio total: "))
descuento = float(input("Ingrese el descuento a aplicar: "))

print(f"Precio total: {precio}, descuento aplicado: {(precio*(descuento/100))}, precio final: {aplicarDescuento(precio, descuento)}")