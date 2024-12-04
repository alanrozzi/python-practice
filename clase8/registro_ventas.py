# Desarrollá un programa que permita registrar las ventas diarias de un comercio durante 5 días.
# Al finalizar, el sistema debe mostrar el total de ventas realizadas en cada día y el promedio de ventas.

# Tips:

# Usá un bucle while que permita al usuario ingresar el monto de las ventas diarias.
# Asegurate de validar que el monto ingresado sea un valor positivo.
# Usá un acumulador para la suma de las ventas.

i=0
j=0
sumador=0
montoDiario=0
montosDiarios=[]

# Usá un bucle while que permita al usuario ingresar el monto de las ventas diarias.
while i < 5:

    montoDiario = float(input("Ingrese el monto valido de la venta del dia: "))
    # Asegurate de validar que el monto ingresado sea un valor positivo.
    while montoDiario < 1:
        montoDiario = float(input("Ingrese el monto valido de la venta del dia: "))

    montosDiarios.append(montoDiario)
    
    # Usá un acumulador para la suma de las ventas.
    sumador += montoDiario
    i+=1

while j < len(montosDiarios):

    print(f"Monto dia {j}: {montosDiarios[j]}")
    
    j+=1

# Al finalizar, el sistema debe mostrar el total de ventas realizadas en cada día y el promedio de ventas.

print(f"\nTotal de ventas: {sumador}")
print(f"Promedio de ventas: {sumador/len(montosDiarios)}")