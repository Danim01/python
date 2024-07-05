import os
# Simular el funcionamiento de una máquina expendedora de dulces. Para este caso es 
# necesario mostrar un menú que contenga las siguientes opciones:  
# Mostrar productos (muestra los productos con su respectivo precio) 
# Comprar producto 
# Insertar crédito 
# Todos los productos de la máquina deben estar almacenados en un archivo (txt, json, etc) y 
# se deben cargar al momento de ejecutar el programa. Cuando se inserte el crédito, se debe 
# mostrar el valor disponible y luego de realizar la compra dicho valor debe ser actualizado. 
# Al final, se debe mostrar un mensaje diciendo si hay regreso de dinero o no y la cantidad. 

rutaDulces = os.path.join("textos_txt", "dulces.txt")

with open(rutaDulces, 'r', encoding='utf-8') as dulces:
    listaPrueba = list()
    maquina = dict()
    
    for linea in dulces:
        # Se esta quitando los saltos de linea de cada linea
        linea = linea.replace("\n", "")
        # Estoy cortando cada linea en los :
        productoYPrecio = linea.split(":")
        # Estoy almacenando en una variable el nombre del producto y le estoy quitando
        # los espacios que pueda tener al inicio y al final 
        nombreProducto = productoYPrecio[0].strip()
        # Estoy almacenando en una variable el valor del producto y le estoy quitando
        # los espacios que pueda tener al inicio y al final 
        precioProducto = int(productoYPrecio[1].strip())

        maquina[nombreProducto] = precioProducto

    productos = {
        1: "bombon",
        2: "gomitas",
        3: "chicle",
        4: "papitas",
        5: "gaseosa"
    }

    print("PRODUCTOS")
    print(maquina)
    print("1: Insertar crédito")
    print("2: Comprar producto\n")

    opcion = 0
    credito = 0
    
    while True:
        opcion = int(input("Ingrese una opción "))
        if opcion == 1:
            credito = int(input("Ingrese su crédito "))
            opcion = 2

        if opcion == 2:
            print(f'\n{productos}\n')
            compra = int(input("Ingrese el número del producto que quiere comprar "))
            if credito == 0:
                credito = int(input("\nPor favor ingrese su credito "))
            producto = productos[compra]
            precio = maquina.get(producto)
            devuelta = credito - precio
            credito = devuelta
            print(f'Su credito es de: {credito}')
            print(f'Su de vuelta es de: {devuelta}')
            print("\nGRACIAS POR SU COMPRA")
            break


