# Escribe una función de Python para comprobar si un número es "perfecto" o no.
# Según Wikipedia:Un número perfecto es un número entero positivo que es igual
# a la suma de sus divisores, es decir, la suma de sus divisores positivos
# excluyendo el número en sí.
# Ejemplo: El primer número perfecto es 6, porque 1, 2 y 3 son sus divisores
# propios, y 1 + 2 + 3 = 6.

def numero_perfecto(numero):
    suma = 0
    for i in range(1, numero-1):
        if numero % i == 0:
            suma = i + suma
    if suma == numero:
        print(f'El número {numero} es perfecto')
    else:
        print(f'El número {numero} no es perfecto')
    

numero_perfecto(8128)
