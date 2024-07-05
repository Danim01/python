import math

# Escriba un programa para calcular el área y el perímetro de los siguientes polígonos. Se debe
# realizar un menú con las siguientes opciones de cálculo: cuadrado, triángulo, rectángulo,
# círculo

areasDict = {
    "rectangulo": lambda base, altura: base * altura,
    "triangulo": lambda base, altura: (base * altura) / 2,
    "circulo": lambda radio: math.pi * radio
}

perimetrosDict = {
    "rectangulo": lambda base, altura: 2 * base + 2 * altura,
    "triangulo": lambda lado1, lado2, lado3: lado1 + lado2 + lado3,
    "circulo": lambda radio: 2 * math.pi * radio
}

menuDict = {
    1: "rectangulo",
    2: "triangulo",
    3: "circulo"
}

print("Elija el poligono que desea calcular\n")
print("1: Rectangulo")
print("2: Triangulo")
print("3: Circulo")
resultado = int(input("\nCual poligono desea calcular "))

caso = menuDict[resultado]
area = areasDict.get(caso)
perimetro = perimetrosDict.get(caso)

areaFigura = 0
perimetroFigura = 0

if caso == "rectangulo":
    baseAreas = int(input(f'\nIngrese la base del {caso} '))
    alturaAreas = int(input(f'Ingrese la altura del {caso} '))
elif caso == "triangulo":
    baseAreas = int(input(f'\nIngrese la base del {caso} '))
    alturaAreas = int(input(f'Ingrese la altura del {caso} '))
    lado1Perimetros = int(input(f'Ingrese el lado 1 de su {caso} '))
    lado2Perimetros = int(input(f'Ingrese el lado 2 de su {caso} '))
    lado3Perimetros = int(input(f'Ingrese el lado 3 de su {caso} '))
elif caso == "circulo":
    radio = int(input(f'\nIngrese el radio del {caso} '))
else:
    print("Ingrese un valor correcto")

if caso == "rectangulo":
    areaFigura = area(baseAreas, alturaAreas)
    perimetroFigura = perimetro(baseAreas, alturaAreas)
elif caso == "triangulo":
    areaFigura = area(baseAreas, alturaAreas)
    perimetroFigura = perimetro(lado1Perimetros, lado2Perimetros, lado3Perimetros)
elif caso == "circulo":
    areaFigura = area(radio)
    perimetroFigura = perimetro(radio)
else:
    print("Ingrese un valor correcto")

print(f'\nEl area de {caso} es: {areaFigura}')
print(f'El perimetro de {caso} es: {perimetroFigura}')