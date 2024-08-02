import json
import os
carpeta_texto = 'textos_json'
ruta = os.path.join(carpeta_texto, 'usuarios.json')
def crear(usuario):
    try:
        with open(ruta, 'r') as archivo:
            datos = json.load(archivo)
    except FileNotFoundError:
        # Si el archivo no existe, iniciar con una lista vacía
        datos = []

    datos.append(usuario)

    with open(ruta, 'w', encoding='utf-8') as archivo2:
        json.dump(datos, archivo2)

    return print("Se agrego el nuevo usuario")

def mostrar(id):
    with open(ruta, 'r') as leer:

        informacion = json.load(leer)
        mostrar = {}
        # Mostrar
        for dato in informacion:
            if dato['id'] == id:
                mostrar = dato
        return mostrar

def actualizar(id, datos_actualizados):
    with open(ruta, 'r') as leer:
        # Actualizar
        informacion = json.load(leer)
        for dato in informacion:
                if dato['id'] == id:
                    # update sirve para actualizar los datos de un diccionario
                    dato.update(datos_actualizados)

    with open(ruta, 'w', encoding='utf-8') as archivo3:
        json.dump(informacion, archivo3)
    
    return print("Se actualizaron los datos")

def eliminar(id):
    with open(ruta, 'r') as leer:
        # Eliminar
        informacion = json.load(leer)
        # voy a crear una nueva lista con todos los datos excepto el que tiene el id que le pase
        informacion = [dato for dato in informacion if dato['id'] != id]

    with open(ruta, 'w', encoding='utf-8') as archivo3:
        json.dump(informacion, archivo3)
    
    return("Se elimino el usuario")


print("CRUD para usuario:")
print("----------------------")
print("1. Crear usuario")
print("2. Mostrar usuario")
print("3. Actualizar usuario")
print("4. Borrar usuario")
print("0. Salir")
print("----------------------")
opcion = int(input("Ingrese la opción deseada: "))

match opcion:
    case 1:
        usuario = {}
        usuario["id"] = input("Ingrese su cedula ")
        usuario["nombre"] = str(input("Ingrese su nombre "))
        usuario["apellido"] = str(input("Ingrese su apellido "))
        usuario["edad"] = input("Ingrese su edad ")
        usuario["correo"] = input("Ingrese su correo ")
        os.system('cls')
        print(crear(usuario))
    case 2:
        id = str(input("Ingrese la cedula del usuario que desea ver "))
        os.system('cls')
        print("Este es el usuario:")
        print(mostrar(id))
    case 3:
        datos_actualizados = {}
        id = str(input("Ingrese la cedula del usuario que desea actualizar "))
        print("----------------------")
        datos_actualizados["id"] = input("Ingrese su cedula ")
        datos_actualizados["nombre"] = str(input("Ingrese su nombre "))
        datos_actualizados["apellido"] = str(input("Ingrese su apellido "))
        datos_actualizados["edad"] = input("Ingrese su edad ")
        datos_actualizados["correo"] = input("Ingrese su correo ")
        os.system('cls')
        print(actualizar(id, datos_actualizados))
    case 4:
        id = str(input("Ingrese la cedula del usuario que desea eliminar "))
        os.system('cls')
        print(eliminar(id))
    case 0:
        os.system('cls')
        print("Fin del programa")
    case _:
        print(" ")

