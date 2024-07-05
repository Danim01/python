# Escriba un programa que pida un número entero y retorne su respectiva 
# representación en binario (no utilizar la función num2bin de Python).
entradaUsuario = int(input("Ingrese el número que desea convertir a binario "))
num = entradaUsuario
binaryDigit = 0
binaryNumber = ""

while num > 0:
    binaryDigit = num % 2
    binaryNumber = str(binaryDigit) + binaryNumber
    num = num // 2

print(f'El número binario de {entradaUsuario} es: {binaryNumber}')