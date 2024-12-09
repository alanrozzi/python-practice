def saludar(nombre="invitado"):
    print("Hola", nombre)

saludar() # Usa el valor por defecto
saludar("Lucía") # Sobrescribe el valor por defecto

#---------------------------------

def sumar(a, b):
    resultado = a + b
    return resultado

total = sumar(5, 3)
print("El total es:", total)
