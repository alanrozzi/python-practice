# Escribir un programa que guarde en variables el
# monto del ingreso de cada uno de los primeros 6
# meses del año.

# Luego, calcular y guardar en otra variable el
# promedio de esos valores.

# Por último, mostrar una leyenda que diga “El
# ingreso promedio en el semestre es de xxxxx”
# donde “xxxxx” es el valor calculado.

enero = 1000;
febrero = 2000;
marzo = 3000;
abril = 4000;
mayo = 5000;
junio = 6000;

suma = enero + febrero + marzo + abril + mayo + junio;
promedio = suma / 6;

print("El ingreso promedio en el semestre es de", promedio);