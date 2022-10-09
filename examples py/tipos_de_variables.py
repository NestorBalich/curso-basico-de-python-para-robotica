# -*- coding: UTF-8 -*-
#Paradigmas Tecnologicos II - Robotica 2020
#Ing Nestor Adrian Balich
#este material es GNU

entero = 27   # entero
print("La variable es del tipo:" , type(entero))

decimal = 3.1416   # decimal con punto flotante
print("La variable es del tipo:" , type(decimal))

cadena = "27.06"   # cadena de caracteres
print("La variable es del tipo:" , type(cadena))

logica = True   # verdadero o falso
print("La variable es del tipo:" , type(logica))

#rangos
rango_numeros = range(2,10)
print("La variable es del tipo:" , type(rango_numeros))
print(rango_numeros)

#definicion de diccionarios
d = { 'marca_auto' : "mazda", 'apellido' : 'gutierrez' }
print("La variable es del tipo:" , type(d))
print (d)
print (d['apellido'])