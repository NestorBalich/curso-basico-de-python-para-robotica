# -*- coding: UTF-8 -*-
#Paradigmas Tecnologicos II - Robotica 2020
#Ing Nestor Adrian Balich
#este material es GNU

f = open("prueba.txt", "w")   #"w" reescribe archivo "a" agrega al final
for nro in range(0,10):
	f.write(str(nro) + " Agrego una linea de texto" + "\n")
f.close()

#open and read the file after the appending:
f = open("prueba.txt", "r")
print(f.read())
f.close()

#graba un archivo

#lee un archivo
archivo=open('prueba.txt','r')
while True:
    slinea = archivo.readline()
    if not slinea:
        break
    else:
        print ('leyendo>> ' , slinea)
archivo.close()

