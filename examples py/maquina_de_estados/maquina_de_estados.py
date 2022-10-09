# -*- coding: UTF-8 -*-
#Paradigmas Tecnologicos II - Robotica 2020
#Ing Nestor Adrian Balich
#este material es GNU
import datetime
import time

g_estado = 0
g_controlador = ""
g_clock_inicio =  0

#creamos una funcion para inicializar el sistema
def setup(): 
	global g_estado
	global g_controlador
	global g_clock_inicio
	g_estado = 0
	g_controlador = "Arduino"
	g_clock_inicio = time.time()
	pass

#retorna el interfavlo desde el inicio en segundos
def get_clock():
	global g_clock_inicio
	
	diferencia = round(time.time() - g_clock_inicio)
	segundos = diferencia % 60 
	#print(segundos)
	return segundos


#creamos una funcion principal
def loop(): 
	global g_estado
	global g_clock_inicio

	while True:
		if (get_clock()> 5):
			g_clock_inicio = time.time() # reinicia el tiempo del intervalo
		
			if g_estado == 0:
				print("robot inicializado")
				#agregar accion 1
				g_estado = 1

			elif g_estado == 1:
				#agregar acion 2
				g_estado = 2
			
			elif g_estado == 2:
				#agregar accion 3
				g_estado = 3

			elif g_estado == 3:
				print("robot tarea terminada")
				#agregar accion 4
				g_estado = 0


if __name__ == "__main__":   #primer linea que se ejecuta del programa
	setup()
	loop()