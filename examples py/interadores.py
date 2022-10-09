# -*- coding: UTF-8 -*-
#Paradigmas Tecnologicos II - Robotica 2020
#Ing Nestor Adrian Balich
#este material es GNU

import math
from math import sqrt

#imprimir caracteres unicode
linea = "Prueba de bucles en python"
cont = 0
while cont < len(linea):
    print (linea[cont])
    cont += 1

for nombre in ['Pepe', 'Ana', 'Juan']:
    print ('Hola, %s.' % nombre)

nombres = ['Pedro', 'Carlos', 'Andrea']

print ('---')

for cont in range(0,3):
    print ('Hola, %s.' % nombres[cont])
