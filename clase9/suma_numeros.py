# Desarrolla un programa en Python que calcule la suma de los números naturales hasta un número dado
# utilizando un bucle for. La suma de los números naturales hasta el número n se define como la suma de todos
# los números enteros positivos desde 1 hasta n.
# Por ejemplo, la suma de los números naturales hasta 6 es 1 + 2 + 3 + 4 + 5 + 6 = 21.

# Tips:

# ¡Usá range()!
# El programa debe pedir un número entero n y devolver la suma de los números naturales hasta n.

suma = 0

limite =  int(input("Ingrese un numero para sumar: "))

for i in range(1, limite+1) :
    print(i)

    suma += i

print(f"Suma total: {suma}")