# Escribe un programa en Python que calcule la
# propina que se debe dejar en un restaurante.

# El script debe solicitar al usuario el monto total de
# la cuenta y el porcentaje de propina que desea
# dejar.

# Utilizando operadores aritméticos, calcula la
# cantidad de propina y el total a pagar (incluyendo
# la propina).

# Finalmente, muestra los resultados en la pantalla.

# Para ingresar texto: input() -> str(): parsea a string.
# para parsear a numeros: float(), int(), etc.
montoCuenta = float(input("Ingrese el monto total de cuenta: "));
porcentajePropina = int(input("Cuanto porcentaje de propina desea dejar?: "));

propinaTotal = montoCuenta * (porcentajePropina/100);

montoTotal = montoCuenta + propinaTotal;

print("La propina a pagar es de:", propinaTotal);
print("El monto total a pagar es de:", montoTotal);