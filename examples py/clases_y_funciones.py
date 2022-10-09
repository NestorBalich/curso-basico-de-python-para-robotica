# -*- coding: UTF-8 -*-
#Paradigmas Tecnologicos II - Robotica 2020
#Ing Nestor Adrian Balich
#este material es GNU

import math
import datetime

g_controlador = "" #variable global
g_now = ""

#*** crea una clase llamada operaciones
class Operaciones:
	
	def cuadrado(selft,x):
		return x**2


	def seno(selft,ang):
		res = math.sin(ang)
		return res
#*** fin de la clase llamada operaciones

#*** crea la funcion fecha
def mostrar_fecha():
	fecha = datetime.datetime.now()
	print ("Ahora es %s." %fecha)
	pass								#no retorna valor, el pass es opcional

#creamos una funcion para inicializar el sistema
def setup(): 
	g_controlador = "Arduino"
	g_now = datetime.datetime.now()
	pass

#creamos una funcion principal
def loop(): 

	class_ejemplo = Operaciones()  #creamos un objeto del tipo clase operaciones
	mostrar_fecha()					# llamamos a la funcion mostrar la fecha
	x = 0
	while x < 4:
		print ("Cuadrados de ", x, " es ", class_ejemplo.cuadrado(x))
		print ("El seno de ", x, " es ", class_ejemplo.seno(x) , "\n")
		x = x  + 1 

if __name__ == "__main__":   #primer linea que se ejecuta del programa
	setup()
	loop()
