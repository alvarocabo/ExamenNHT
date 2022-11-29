"""
Hacer una calculadora en Python sin utilizar operadores (+,-,etc). El cual recibirá inputs de entrada y una salida (resultado)

Se que te surgirán muchas preguntas/dudas en el camino para este test, pero en este caso, el camino lo elegirás tu. La intención con este ejercicio es conocer mas a fondo 
tu paradigma y tomaremos en cuenta aspectos como:
	1.- Archivos entregables.
	2.- Código Limpio, principios solid (de los que se puedan aplicar).
	3.- Virtualizacion (conocimientos pipenv o vituralenv, etc.)

"""

from signal import signal, SIGINT
from lib import operators, utilities

def handler(signal_received, frame):
    print('\nExiting successfully')
    exit(0)

def menu():
    counter =0
    print("PyCalc! - Please give an operation")

    while(True):
        if(counter%15==0):
            recordatorio()
        a= input("PyCalc>" )
        tk =utilities.lexer(a)
        if(tk is not None):
            print(utilities.parser(tk))
        else:
            print("CARACTER NO NUMERICO")
        counter+=1

def recordatorio():
    print("*Hint! -> Puede parar el programa con Ctr+C")

if(__name__ == "__main__"):
    signal(SIGINT, handler)
    menu()