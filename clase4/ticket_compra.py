# Escribir un programa que solicite el nombre, la
# cantidad y el valor unitario de tres productos.

# Luego, debe calcular el importe de IVA (21%)
# de cada producto.

# Por último, debe mostrar en la terminal el
# ticket de la operación con todos los datos de la
# compra.

iva = 21;

############# ENTRADA

# nombreProducto1 = input("Ingrese el nombre el primero producto: ");
# cantidadProducto1 = int(input("Ingrese la cantidad del primero producto: "));
# valorProducto1 = float(input("Ingrese el valor del primero producto: "));

# nombreProducto2 = input("\nIngrese el nombre el segundo producto: ");
# cantidadProducto2 = int(input("Ingrese la cantidad del segundo producto: "));
# valorProducto2 = float(input("Ingrese el valor del segundo producto: "));

# nombreProducto3 = input("\nIngrese el nombre el tercer producto: ");
# cantidadProducto3 = int(input("Ingrese la cantidad del tercer producto: "));
# valorProducto3 = float(input("Ingrese el valor del tercer producto: "));


nombreProducto1 = "prod1";
cantidadProducto1 = 1;
valorProducto1 = 100;

nombreProducto2 = "prod2";
cantidadProducto2 = 2;
valorProducto2 = 100;

nombreProducto3 = "prod2";
cantidadProducto3 = 3;
valorProducto3 = 100;


############# PROCESO

ivaProducto1 = (valorProducto1 * iva) / 100;
totalIva1 = valorProducto1 + ivaProducto1; #precio + iva
totalProd1 = totalIva1 * cantidadProducto1;

ivaProducto2 = (valorProducto2 * iva) / 100;
totalIva2 = valorProducto2 + ivaProducto2; #precio + iva
totalProd2 = totalIva2 * cantidadProducto2;

ivaProducto3 = (valorProducto3 * iva) / 100;
totalIva3 = valorProducto3 + ivaProducto3; #precio + iva
totalProd3 = totalIva3 * cantidadProducto3;

############# SALIDA

print("Nombre\tPrecio\tCant\tIva(21%)\tTotal");
print(nombreProducto1, "\t", valorProducto1, "\t", cantidadProducto1, "\t", ivaProducto1, "\t\t", totalProd1);
print(nombreProducto2, "\t", valorProducto2, "\t", cantidadProducto2, "\t", ivaProducto2, "\t\t", totalProd2);
print(nombreProducto3, "\t", valorProducto3, "\t", cantidadProducto3, "\t", ivaProducto3, "\t\t", totalProd3);