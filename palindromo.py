# Un palíndromo es una palabra o frase cuyas letras están dispuestas de tal manera que es 
# posible leerla de izquierda a derecha y derecha a izquierda obteniendo el mismo resultado. 
# Ejemplos de estas palabras son: anilina, luz azul, oro, 1001, 202, entre otras. 

# El método .replace lo que hace es reemplazarme lo que yo quiero por otra cosa
# recibe como primer parámetro el valor de lo que ya no quiero tener y como
# segundo parámetro recibe por lo que quiero cambiar 
palabra = "luz azul".replace(" ", "")


# El [:: -1] en un slicing que recibe 3 parámetros, el primer parámetro es desde donde quiero empezar a cortar,
# el segundo parámetro es hasta donde quiero cortar y el tercer parámetro es como quiero recorrer
# en este caso no ponemos los dos primeros parámetros por que queremos que recorra todo el string
# como tercer parámetro ponemos el -1 para recorrer todo al revés
palabraInvertida = palabra[::-1]

if palabra == palabraInvertida:
    print(f'Su palabra {palabra} es un palíndromo')
else:
    print(f'Su palabra {palabra} no es un palíndromo')
