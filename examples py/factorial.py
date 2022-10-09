# -*- coding: UTF-8 -*-
#Paradigmas Tecnologicos II - Robotica 2020
#Ing Nestor Adrian Balich
#este material es GNU

def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)


numero = -1
fac = 0
 
numero = 10 #int(input("Numero "))
fac = factorial(numero)
 
print ("El factorial de " + str(numero) + " es " + str(fac))


