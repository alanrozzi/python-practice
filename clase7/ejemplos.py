#LISTAS
#se pueden mezclar tipos de datos

#len(): cant de caracteres o valores en lista.

meses = ["enero", "febrero", "marzo", "abril"]
temperatura = [12, 32.7, 4.1, 2]

#metodos se acceden por el nombre de la lista:

meses.append("mayo")
print(meses)

# meses.remove("abril")
# print(meses)

# del meses[2]
# print(meses)

#tupla: lista inmutable, no se puede modificar, se puede
#estandarizar un sistema de datos, ocupa menos espacio en memoria
apellidos = ("Monte", "Aguilar")


#recorrer lista:

i=0

while i < len(meses):
    print(f"Indice {i}: {meses[i]}")
    i+=1

#se pueden generar listas de listas.

listProductos = [
    ["harina", 2, 400],
    ["pan", 3, 100]
]