# Paradigmas Tecnológicos II - Robótica 2020
# Universidad Abierta Interamericana
# Profesor: Ing. Nestor Balich
# Alumno: Sanguin Martin
# Fecha: 07/09/2020
# Detalle del programa: Ingresando una palabra el mismo detecta si la misma es palindromo o no.
import sys

palabraAverificar = input("Ingresa una palabra: ")
i = 0
j = len(palabraAverificar)-1
esPalindromo = True

while(j - i > 0):
    esPalindromo = esPalindromo and (palabraAverificar[i] == palabraAverificar[j])
    i += 1
    j -= 1
    if(esPalindromo):
        print("¡La palabra " , palabraAverificar , " es palindromo!")
    else:
        print("¡La palabra " , palabraAverificar , " no es palindromo!")