# -*- coding: UTF-8 -*-
#Paradigmas Tecnologicos II - Robotica 2020
#Ing Nestor Adrian Balich
#este material es GNU

import datetime
import time

fecha = datetime.datetime.now()

print ("Ahora es %s." %fecha)

inicio = time.time()

diferencia = round(time.time() - inicio)
segundos = diferencia % 60 
try:
	while (segundos < 5):
		diferencia = round(time.time() - inicio)
		segundos = diferencia % 60  # calcula los segundos
		print ('Tiempo ejecución '+ str(segundos) + " segundos")

except TypeError as err:
        print('ERROR:', err)

