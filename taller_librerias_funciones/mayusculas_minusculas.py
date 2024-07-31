import re

# Escriba una función que reciba una cadena de texto y retorne la cantidad de
# mayúsculas y minúsculas que contiene.
# Ejemplo:
# Texto de entrada: Era Una Mañana Soleada
# Mayúsculas = 4
# Minúsculas = 14

def cantidad_mayusculas_minusculas(texto):
    mayusculas = 0
    minusculas = 0
    patron_mayusculas = r'^[A-Z]$'
    patron_minusculas = r'^[a-z]$'
    for letra in texto:
        if re.match(patron_mayusculas, letra):
            mayusculas += 1

    for letra in texto:
        if re.match(patron_minusculas, letra):
            minusculas += 1

    return {
        "mayusculas": mayusculas, 
        "minusculas": minusculas
        }

texto = str(input("Escriba su oración "))
respuesta = cantidad_mayusculas_minusculas(texto)

print(f'La oración: {texto} tiene:')
print(f'Mayúsculas = {respuesta["mayusculas"]}')
print(f'Minúsculas = {respuesta["minusculas"]}')
        

    