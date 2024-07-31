# Crea un programa que calcule el daño de un ataque durante una batalla Pokémon. La 
# fórmula será la siguiente:  
# daño = 50 * (ataque / defensa) * efectividad 
# Efectividad: x2 (súper efectivo), x1 (neutral), x0.5 (no es muy efectivo) 
# Sólo hay 4 tipos de Pokémon: Agua, Fuego, Planta y Eléctrico  
# (buscar su efectividad) 
# El programa recibe los siguientes parámetros: 
# Tipo del Pokémon atacante. 
# Tipo del Pokémon defensor. 
# Ataque: Entre 1 y 100. 
# Defensa: Entre 1 y 100.
# Efectividad = x2 (super efectivo), x1 (neutral), x0.5 (no es muy efectivo) 

matrizEfectividad = [
    [1,	2, 0.5,	1],
    [0.5, 0.5, 2, 1],
    [2, 0.5, 0.5, 0.5],
    [2, 1, 0.5, 0.5]
]

print("POKÉMONES\n")
print("Atacantes")
print("1: Agua")
print("2: Fuego")
print("3: Planta")
print("4: Electrico")
atacante = int(input("\nIngrese el número de su Pokémon atacante "))


print("\nDefensor")
print("1: Agua")
print("2: Fuego")
print("3: Planta")
print("4: Electrico")
defensor = int(input("\nIngrese el número de su Pokémon defensor "))
ataque = int(input("\nIngrese el valor de su ataque, recuerde que es entre 1 y 100 "))
defensa = int(input("Ingrese el valor de su defensa, recuerde que es entre 1 y 100 "))

efectividadAtacante = atacante - 1
efectividadDefensor = defensor - 1
efectividad = matrizEfectividad[efectividadAtacante][efectividadDefensor]

dano = 50 * (ataque / defensa) * efectividad

print(f'El daño de la pelea fue de: {dano}')

