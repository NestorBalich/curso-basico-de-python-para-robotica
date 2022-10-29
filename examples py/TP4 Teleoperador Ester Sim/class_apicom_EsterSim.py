# -*- coding: UTF-8 -*-
#23-10-2022 clase de comunicacion simulador Ester Sim
#by Nestor Balich
import requests
import os

class apicom_EsterSim:
    def __init__(self, url_server,apikey,user_id,id,title,debug=False):
        self.url_server = url_server
        self.apikey = apikey
        self.user_id = user_id
        self.key = ""
        self.id = id
        self.title = title
        self.debug = debug

    def req_put(self,key,comando,valor):
        #robot_name = "Robot" + str(self.robot_id)
        data = {
            "apikey": self.apikey,
            "user_id":  self.user_id,
            "id":self.id,
            "title":self.title,
            "key":key,
            "command":comando,
            "value":valor
        }
        response = requests.put(self.url_server, json=data)

        if self.debug:
            print("Status code: ", response.status_code)
            print(response.json())
            return response.json()

    def req_post(self,comando,valor):
        robot_name = "Robot" + str(self.id)
        data = {
            "apikey": self.apikey,
            "user_id":  self.user_id,
            "id":self.id,
            "title":self.title,
            "key":self.key,
            "command":comando,
            "value":valor
        }
        response = requests.post(self.url_server, json=data)
        if self.debug:
            print("Status code: ", response.status_code)
            print(response.json())

        return response.json()

    #busca la clave del robot en la primer conexion y luego la guarda en disco
    #si se necesita blanque borre el archivo e informe a profesor para que genere una nueva clave
    def get_object_key(self):
        if os.path.isfile('key.txt'):
            f = open("key.txt", "r")
            key = f.read()  #lee la linea y elimina salto de linea al final
            f.close()
            if self.debug:
                print(f"Clave leida desde archivo: {key}")
        else:   
            #obtenemos la clave del robot solo una vez y la guardamos en disco
        
            jres= self.req_post("get_object_key",self.id)
            key = jres['key'] 
            if (key != ''):
                if self.debug:
                    print(f"guarda esta clave que es unica para vos {self.key}")
                f = open("key.txt", "w")   #"w" reescribe archivo "a" agrega al final
                f.write(key)
                f.close()

        return key    