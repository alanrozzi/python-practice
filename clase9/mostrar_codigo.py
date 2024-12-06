# En un sistema de inventario, cada producto tiene un código que lo identifica. Escribí un programa que permita
# ingresar los códigos de 4 productos y luego mostrálos uno por uno, junto con su posición en la lista.

# Ejemplo: si los códigos ingresados son "P001",
# "P002", "P003", "P004", el programa debe mostrar:

# Utilizá un bucle for y range() para recorrer los códigos e imprimirlos.


codigos = []

for i in range(4) :
    codigos.append(input(f"Ingrese el codigo n{i}: "))
    
# for codigo in codigos :
#     print(f"Producto  : {codigo}")

for i in range(4) :
    print(f"Producto {i} : {codigos[i]}")