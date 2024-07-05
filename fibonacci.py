# Escribe un programa que imprima los 50 primeros números de la sucesión de Fibonacci 
# empezando en 0. Nota: 
# NOTA: La serie Fibonacci se compone por una sucesión de números en la que el siguiente 
# siempre es la suma de los dos anteriores. Ej: 0, 1, 1, 2, 3, 5, 8, 13...
fibonnaci = []

def imprimirFibonnaci(maximo):
    fibonnaci.append(0)
    fibonnaci.append(1)

    for i in range (2, maximo):
        fibonnaci.append(fibonnaci[i - 1] + fibonnaci[i - 2])
    
    return fibonnaci


numero = int(input("Ingrese la cantidad de numeros que quiere saber de la serie de fibonnaci\n"))

print(imprimirFibonnaci(numero))