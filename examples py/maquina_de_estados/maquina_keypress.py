# -*- coding: UTF-8 -*-
#Paradigmas Tecnologicos II - Robotica 2022
#Ing Nestor Adrian Balich
#este material es GNU
import os
import keyboard
import time

g_estado = 0
g_controlador = ""
g_clock_inicio =  0

#creamos una funcion para inicializar el sistema
def setup(): 
	global g_estado
	g_estado = 0
	pass


#creamos una funcion principal
def loop(): 
    global g_estado 
    g_estado = 1
    tecla = ''
    
    while True:
            
            if g_estado == 1:
                os.system("cls")
                print(f"Ingresa número del 0 al 3 para cambiar de estado, ahora estado \n")
                print(f"Sistema iniciado estado {g_estado}\n")
				#agregar accion 1
                if tecla == "2":
                    g_estado = 2
                    print(f"Pasando al estado {g_estado} tecla presionada {tecla}\n")

            elif g_estado == 2:
				#agregar acion 2
                if tecla == '3':
                    g_estado = 3
                    print(f"Pasando al estado {g_estado} tecla presionada {tecla}\n")
                    
			
            elif g_estado == 3:
				#agregar accion 3
                if tecla == '4':
                    g_estado = 4
                    print(f"Pasando al estado {g_estado} tecla presionada {tecla}\n")
                    

            elif g_estado == 4:
				#agregar accion 4
                if tecla == '1':
                    g_estado = 1
                    #print(f"Estado {g_estado} tecla presionada {tecla}\n")
                   
            tecla = keyboard.read_key() 

if __name__ == "__main__":   #primer linea que se ejecuta del programa
	setup()
	loop()