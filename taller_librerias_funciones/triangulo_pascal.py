# Escriba una función que imprima las primeras N filas del triángulo de Pascal

def triangulo_pascal(filas):
    espacios1 = filas 
    for i in range(1, 3):
        espacios1 -= 1
        base = " " * (espacios1) + "1" * (i)
        print(base)
    espacios2 = filas - 2
    for i in range(3, filas + 1):
        espacios2 -= 1
        print(" " * (espacios2) + "1" + " " * (i - 2) + "1")
        

triangulo_pascal(4)