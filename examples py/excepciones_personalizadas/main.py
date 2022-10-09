# # -*- coding: UTF-8 -*-
# Ejemplo de excepciones customizadas 7/9/2020
# Paradigmas tecnologicos II - Robotica UAI , prof Nestor Balich
# Realizado por:
# Alumno: Ezequiel Ortiz
# Alumno: Facundo Barros

import excepciones as exc

nombre = input("Ingrese Nombre: ")
apellido = input("Ingrese Apellido: ")

try:
    if (nombre.lower() == "ezequiel" and apellido.lower() == "ortiz") or\
            (nombre.lower() == "facundo" and apellido.lower() == "barros"):
        try:
            edad = int(input("Bueno, pero falta tu edad. Ingresa tu Edad: "))
            if edad == 24 or edad == 31:
                print("Estas Autorizado!!!!!")
            else:
                raise exc.NoAutorizadoException()
        except ValueError as exc:
            print("Ingrese un numero valido.")
    else:
        raise exc.NoAutorizadoException()
except exc.NoAutorizadoException as exc:
    print(exc)
except Exception as exc:
    print(exc)
