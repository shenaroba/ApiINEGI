from email import header
from lib2to3.pgen2 import token
from os import access
from tokenize import String
import requests
import json

URL="https://www.inegi.org.mx/app/api/denue/v1/consulta/Buscar/"

headers={'conten-type' : 'aplication/json', 'access-token' : '46a2aadf-1d0b-4dce-adb2-90750125c473'}

response=requests.get(URL)
sc=response.status_code
print(sc)
if sc == 200:
    tbus=input("que desea buscar:")
    lat=input("Ingrese latitud:")
    lon=input("ingrese longitud:")
    dis=input("ingrese distancia de busqueda:")
    accesstoken='46a2aadf-1d0b-4dce-adb2-90750125c473'

    URL2=URL+tbus+'/'+lat+'/'+lon+'/'+dis+'/'+accesstoken

    response2=requests.post(URL2)
    #response1=requests.get(URL2)
    print(response2)
    print(response2.content)



    
else:
    print("No se pudo conectar con la APi, error")