import math
# Crear un programa que imprima en pantalla una figura
n = 11

if n % 2 == 0:
    n += 1

for i in range (math.ceil(n / 2)):
    #(n - 2 * i) la i me representa a cada fila y al multiplicarlo 
    # por 2 me da la cantidad de * que debo quitar por fila
    print( " " * i + "*" * (n - 2 * i))

# Necesito que mi código vaya hacia atrás para ir imprimiendo la otra mitad
# del reloj, ya que en la parte de arriba se imprimió la mitad mas uno y necesito 
# imprimir la otra mitad 
# En el math le resto 1 para que mi código no empiece exactamente 
# donde termino la parte de arriba, si no que empiece en la linea anterior a esa
# para que así se unan, es decir el código de arriba termino en un * y yo quiero que
# este empiece en tres * para poder que se cree el reloj de arena.
for i in range (math.floor(n / 2) -1, -1, -1):
   print( " " * i + "*" * (n - 2 * i))




