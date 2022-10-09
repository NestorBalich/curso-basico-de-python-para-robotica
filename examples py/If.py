#Paradigmas Tecnologicos II - Robotica 2020
#Ing Nestor Adrian Balich
#este material es GNU

import datetime

ahora = "Fecha Hora Actual es: %s ." % datetime.datetime.now()

nombre = input('Ingresa tu nombre: ')
if nombre  ==  'Pepe':
    Apellido  = 'lopez'
    
    print  (ahora, '> Pepe Lopez ingreso permitido')
else:
    print (ahora, '> Solo se permite acceso a pepe')
