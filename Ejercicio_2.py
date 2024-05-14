import random
from datetime import datetime

def obtener_numero_aleatorio():
    return random.randint(1, 50)

def validar_numero(numero):
    try:
        numero = int(numero)
        if numero > 0 and numero < 100:
            return True
        else:
            return False
    except ValueError:
        return False

def adivina():
    numero_aleatorio = obtener_numero_aleatorio()
    print("Adivina el número secreto (entre 1 y 50):")

    def validar_adivina():
        while True:
            numero = input("Introduce un número: ")
            if validar_numero(numero):
                numero = int(numero)
                if numero == numero_aleatorio:
                    print("¡Has ganado!")
                    ahora = datetime.now()
                    print("Fecha y hora de acierto:", ahora.strftime("%Y-%m-%d %H:%M"))
                    break
                elif numero < numero_aleatorio:
                    print("El número secreto es mayor.")
                else:
                    print("El número secreto es menor.")
            else:
                print("Por favor, introduce un número entero entre 1 y 50.")

    return validar_adivina

def decorador_mensaje(func):
    def wrapper():
        print("¡Adivina el número secreto!")
        func()
        print("¡El juego ha terminado!")
    return wrapper
