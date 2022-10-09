#Paradigmas Tecnologicos II - Robotica 2020
#Ing Nestor Adrian Balich
#este material es GNU

numero = 3
while (numero >= 0) :
	try:
		division = 10 / numero
		numero = numero - 1
	except (ZeroDivisionError, ValueError ):  #intercepta el error
		print ("Error de división por cero")
		break							     #sale del bucle		
   	
	print ("División correcta =", division)	 #si la division es correcta

while (numero >= 0) :
	try:
		numero = int(input("Ingrese un numero: "))
	except ValueError as err: #intercepta el error
		print (f"Error debe ingresar un numero ({err})")
		continue							     #1sale del bucle		
	else:
		print(f'Ingreso correctamente un: {numero}')
		break
