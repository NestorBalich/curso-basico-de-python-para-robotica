import requests
import json

#https://nationalize.io/
nombre=input("Ingrese el nombre deseado: ")
conversionSexo={"male":"masculino", "female":"femenino"}

url="https://api.nationalize.io?name="+nombre
resp=requests.get(url)
if resp:
    print(resp.text)
    dict=resp.json()
    pais = dict["country"][0]["country_id"]
    probabilidad = dict["country"][0]["probability"]
    print(f"\nPais:{pais} probability:{probabilidad}")
