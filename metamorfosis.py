import os
import re
# Escriba un programa que lea el texto que se encuentra en el archivo metamorfosis.txt y 
# retorne la cantidad de veces que se encuentran repetidas las palabras:  
# El resultado de este ejercicio se debe guardar en un archivo de su elección.

# Utilizando el texto de la metamorfosis, determinar: 
# Número total de palabras. 
# Longitud media de las palabras. 
# Número de oraciones del texto (cada vez que aparecen un punto). 
# Encuentre la palabra más larga. 
# hh

carpetaTextos = "textos_txt"
rutaMetamorfosis = os.path.join(carpetaTextos, "metamorfosis.txt")
rutaResultado = os.path.join(carpetaTextos, "resultado.md")

with open(rutaMetamorfosis, 'r', encoding='utf-8') as metamorfosis, \
     open(rutaResultado, 'w', encoding='utf-8') as respuesta:

    repetido = dict()
    cantidadPalabras = 0
    sumaLongitud = 0
    orationsNumber = 0
    for line in metamorfosis:
        orationsNumber += line.count(".")
        # A cada linea del texto le estoy quitando todos los símbolos
        # como primer parámetro recibe la expresión regular, como segundo parámetro
        # recibe por lo que quiero cambiar y como tercero recibe donde esta guardado el texto 
        line = re.sub(r'[^a-zA-ZáéíóúüñÁÉÍÓÚÜÑ\s]', "", line)
        # Se esta convirtiendo la cada linea minúscula 
        line = line.lower()
        # Agrega cada una de las palabras del texto a esta variable ya que con el
        # .split le estamos diciendo que la referencia para cortar las palabras es un espacio
        # ya que no le estamos dando una referencia para cortar las palabras
        words = line.split()
        for word in words:
            cantidadPalabras += 1
            sumaLongitud += len(word)
            # Esta buscando la palabra en el diccionario y si no la encuentra 
            # la agrega al diccionario con el valor en 0 y si ya existe 
            # le va a sumar y ese va a ser el nuevo valor de la key
            repetido[word] = repetido.get(word, 0) + 1
    
    palabraLarga = ""
    for palabra in repetido.keys():
        if len(palabra) > len(palabraLarga):
            palabraLarga = palabra

    mediaLongitud = sumaLongitud / cantidadPalabras

    textoParaEscribir = "# Resultados:\n"

    textoParaEscribir += "Aquí están todas las palabras y la cantidad de veces que se encuentran repetidas del archivo de metamorfosis \n\n"

    textoParaEscribir += f'El número total de palabras es: **{cantidadPalabras}**<br/>\n'

    textoParaEscribir += f'La longitud media de las palabras es: **{round(mediaLongitud, 2)}**<br/>\n'

    textoParaEscribir += f'El número de oraciones del texto es: **{orationsNumber}**<br/>\n'

    textoParaEscribir += f'La palabra más larga del texto es **{palabraLarga}** y su longitud es de **{len(palabraLarga)}**\n\n'

    textoParaEscribir += "|Palabra|Cantidad|\n"
    # los : me sirve para decir el tipo de alineación del texto
    textoParaEscribir += "|:---|:---:|\n"
    for palabra, valor in repetido.items():
        textoParaEscribir += f'|{palabra.capitalize()}| {valor}|\n'

    respuesta.write(textoParaEscribir)
