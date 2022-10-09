# LRFUAI by Nestor Balich License GCC  2020
# Universidad Abierta Interamericana Laboratorio de robotica fisica
# https://innovativalab.com.ar youtube: NeoroboticTV
# Importamos la libreira de PySerial pip install pyserial
import serial

#importamos  la libreria time para leer cada un segundo 
import time

#Abrimos el puerto del arduino a 9600
puerto = 'COM4'
PuertoSerie = serial.Serial(puerto, 9600)

# Provocamos un reseteo manual de la placa para leer con el buffer limpio
PuertoSerie.setDTR(False)
time.sleep(1)
PuertoSerie.flushInput()
PuertoSerie.setDTR(True)

# Import library and create instance of REST client.
from Adafruit_IO import Client
aio = Client('tu usario', 'tu key')

#enviado mensaje
aio.send('mensaje', 'interface python para arduino uno conectado al '+ puerto)

#esperando datos
while PuertoSerie:
    try:

        datosASCII = PuertoSerie.readline() # lee el dato enviado por arduino
        #print("datosASCII", str(datosASCII)) 

        #armar  el numero y chequea si cada chat  es un numero de 0 a 9
        bNoEsNumero = True
        datosCaracter = ""
        for valor in datosASCII:
            datosCaracter = datosCaracter + chr(valor)
            if (  chr(valor).isdigit() == False):
            	bNoEsNumero = False
            	break

        print("Dato recibido de arduino", str(datosCaracter))  

        if not bNoEsNumero:
        	PuertoSerie.flushInput()
        	
        	aio.send('temperatura', datosCaracter) #nivel iluminacion

        	data = aio.receive('boton')
        	led = str(data.value)   #convertimos a string
        	if (led  == 'ON'):
        		PuertoSerie.write(b'1')   #envia orden de encender led al arduino
        	elif (led  == "OFF"):
        		PuertoSerie.write(b'0')   #envia orden de apagar led al arduino
       		

        time.sleep(5)

    except KeyboardInterrupt:
        break
	

PuertoSerie.close()


