import requests
from bs4 import BeautifulSoup
import json
import os

url = "https://es.vuejs.org/v2/guide/"

respuesta = requests.get(url)

pagina = BeautifulSoup(respuesta.text, 'html.parser')

contenido = pagina.find(class_="content guide with-sidebar index-guide")
parrafos = contenido.find_all('p')

informacion = {}
# enumerate es una función que me ayuda a enumerar una lista
# start me indica desde que numero la voy a empezar a enumerar 
for i, p in enumerate(parrafos, start=1):
    parrafo = (f'Parrafo {i}')
    # p.text solo me imprime la información de los parrafos sin la estructura html
    informacion[f'Parrafo {i}'] = p.text
#        (f"Párrafo {i}: {p.text}")

carpeta_texto = 'textos_json'
ruta = os.path.join(carpeta_texto, 'pagina_vue.json')
with open(ruta, 'w', encoding='utf-8') as archivo:
    json.dump(informacion, archivo)
    print("Se agrego la información en tu archivo json")
