# Crea un programa que solicite al usuario dos
# números enteros.

# Realiza las siguientes operaciones: suma,
# resta, multiplicación, y módulo.

# Muestra el resultado de cada operación en un
# formato claro y amigable.

# Asegúrate de incluir mensajes personalizados que
# expliquen cada resultado, por ejemplo: "La suma
# de tus números es: X".

numero1 = float(input("Ingrese el numero 1: "));
numero2 = float(input("Ingrese el numero 2: "));

suma = numero1 + numero2;
resta = numero1 - numero2;
multiplicacion = numero1 * numero2;
modulo = numero1 % numero2;

print("La suma tus números es:", suma);
print("La resta tus números es:", resta);
print("La multiplicacion tus números es:", multiplicacion);
print("El modulo tus números es:", modulo);