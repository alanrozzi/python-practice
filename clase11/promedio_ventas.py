# Desarrollá un programa que permita calcular el promedio de ventas de la tienda. Para esto:

# Creá una función que reciba como parámetro una lista de ventas diarias y devuelva el promedio de esas ventas.

# Solicitá a la persona que ingrese las ventas de cada día durante una semana (7 días).
# Usá la función para calcular y
# mostrar el promedio de ventas al finalizar.

def calcularPromedio(ventasDiarias):
    return sum(ventasDiarias)/len(ventasDiarias)

def agregarVentas():
    ventasDiarias = []
    for i in range(1, 8):
        venta = int(input(f"Ingrese el valor de la venta {i}: "))
        ventasDiarias.append(venta)
    #print(f"la sum: {sum(ventasDiarias)}")
    return ventasDiarias

print(f"Promedio de ventas: {calcularPromedio(agregarVentas())}")
