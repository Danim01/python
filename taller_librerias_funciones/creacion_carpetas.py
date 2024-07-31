import os
import glob

# Usando el módulo de sistema operativo, cree un directorio llamado ventas.
# Luego, en el directorio de ventas, cree 12 capetas para cada mes con los
# nombres...
# 01_ventas,
# 02_ventas,
# 03_ventas,
# ....
# 12_ventas
# Finalmente, imprima una lista con los nombres de las carpetas que fueron
# creadas dentro del directorio de ventas.

os.mkdir("taller_librerias_funciones/ventas")

for i in range(1, 13):
    nombre_carpeta = str(i).rjust(2, "0") + ("_ventas")
    os.mkdir(f'taller_librerias_funciones/ventas/{nombre_carpeta}')

os.chdir("./taller_librerias_funciones/ventas")
lista_archivos = glob.glob('*')
print(lista_archivos)



