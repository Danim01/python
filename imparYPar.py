# Desarrolle un programa que permita determinar si un número es primo y/o par. 

entradaUsuario = int(input("Ingrese un número "))
number = entradaUsuario

while True:
    for i in range(number):
        esPrimo = True
        if number == 1:
            esPrimo = False

        for p in range(2, number - 1):
            if number % p == 0:
                esPrimo = False 

    if esPrimo == True or number == 1:
        print(f'El número {number} es PRIMO')
        break
    elif number % 2 == 0:
        print(f'El número {number} es PAR')
        break
    else: 
        print(f'El número {number} no es ni primo ni par')
        break

