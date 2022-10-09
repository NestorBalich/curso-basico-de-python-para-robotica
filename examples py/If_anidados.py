# -*- coding: UTF-8 -*-
#Paradigmas Tecnologicos II - Robotica 2020
#Ing Nestor Adrian Balich
#este material es GNU

flag= True
try:
  numero = int(input("Ingrese un número por favor: "))
except (ValueError, TypeError, NameError):
  print ("Cometió un error. Usted a ingresado un dato no númerico ")
  flag = False

if flag:
    if numero == 7:
        print ("El número es siete " , numero)
    elif numero > 10:
        print ("El número es mayor a siete")
    else:
        print ("El número es menor a siete")
