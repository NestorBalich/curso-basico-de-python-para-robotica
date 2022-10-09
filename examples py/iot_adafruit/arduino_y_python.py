# LRFUAI by Nestor Balich License GCC 2020
# https://innovativalab.com.ar
# https://io.adafruit.com/
# importamos  la libreria time para leer cada un segundo
# importamos la libreira de PySerial pip install pyserial
import serial

#importamos  la libreria time para leer cada un segundo 
import time

#Abrimos el puerto del arduino a 9600
PuertoSerie = serial.Serial('COM4', 9600)

# Provocamos un reseteo manual de la placa para leer con el buffer limpio
PuertoSerie.setDTR(False)
time.sleep(1) 
PuertoSerie.flushInput()
PuertoSerie.setDTR(True)


#esperando datos
while PuertoSerie:
    try:

        datosASCII = PuertoSerie.readline() # lee el dato enviado por arduino

        #arma  el numero y chequea si cada chat  es un numero de 0 a 9
        bNoEsNumero = True
        datosCaracter = ""
        for valor in datosASCII:
            datosCaracter = datosCaracter + chr(valor)
            if (  chr(valor).isdigit() == False):
            	bNoEsNumero = False
            	break

        print("Dato recibido", str(datosCaracter))  

        if not bNoEsNumero:
        	numero = float(datosCaracter)  #tranforma la cadena de caracter a numero
        	if (numero > 200):
        		print("Necesita luz")
        		PuertoSerie.write(b'1')   #envia orden de encender led al arduino
        	else:
        		PuertoSerie.write(b'0')   #envia orden de apagar led al arduino

        time.sleep(1)

    except KeyboardInterrupt:
        break
	

PuertoSerie.close()


