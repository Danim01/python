import glob
import os

# Usando el módulo os para manejo del sistema operativo, cree una lista que
# contenga nombres de archivos en su directorio de trabajo que tengan extensión
# .py. Ordene esta lista alfabéticamente e imprímala en consola.


def lista_archivos():
    # Esta cambiando de carpeta, ya que de entrada abre la carpeta donde estoy trabajando
    os.chdir("./taller_librerias_funciones")

    lista_archivos = glob.glob('*.py')
    print(lista_archivos)
    lista_archivos.sort()
    return lista_archivos

print(lista_archivos())