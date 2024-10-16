# A partir de la cantidad de litros de combustible que
# consume un coche por cada 100 km de recorrido,
# el costo de cada litro de combustible y la longitud
# del viaje realizado (en kilómetros), muestra un
# detalle de los litros consumidos y el dinero
# gastado.

costoLitro = 1000;
kmRecorridos = 200;

consumo = 5/100;

litrosConsumidos = 0;
gastoTotal = 0;

# 5 litros cada 100 km

litrosConsumidos = 200 * consumo;
gastoTotal = litrosConsumidos * costoLitro;


print("La cantidad de litros consumidos es de:", litrosConsumidos);
print("El dinero gastado es de :", gastoTotal);