# -*- coding: UTF-8 -*-
#Paradigmas Tecnologicos II - Robotica 2020
#Ing Nestor Adrian Balich
#este material es GNU

g_variable_global = 20
VALOR_CONSTANTE = 10
a = "hola"

def suma():
	global g_variable_global  # para poder cambiar el valor de una variable global
	suma =  g_variable_global + VALOR_CONSTANTE + 10

	a = 10   #crea  y asigana el valor de una variable local
	print ("print a dentro de función: ", a)
	return suma

print(suma())
print ("print a fuera de la función de función: ", a)
