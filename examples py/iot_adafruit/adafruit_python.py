# LRFUAI by Nestor Balich License GCC 2020
# https://innovativalab.com.ar
# https://io.adafruit.com/
#importamos  la libreria time para leer cada un segundo
import time

# Import library and create instance of REST client.
from Adafruit_IO import Client
aio = Client('tu usuario', 'tu key')

# Send the value 100 to a feed called 'temperatura'.
aio.send('temperatura', 60)

# Retrieve the most recent value from the feed 'temperatura'.
# Access the value by reading the `value` property on the returned Data object.
# Note that all values retrieved from IO are strings so you might need to convert
# them to an int or numeric type if you expect a number.
data = aio.receive('temperatura')
print('Received value: {0}'.format(data.value))

#enviado mensaje
aio.send('mensaje', 'python 2 conectado')


#esperando datos
while True:
	data = aio.receive('boton')
	temp = str(data.value)   #convertimos a string
	if (temp  == 'ON'):
		print("Led encendido")
	elif (temp  == "OFF"):
		print("Led apagado")
	else:
	   print('Received value: {0}'.format(data.value))
	time.sleep(1) 


