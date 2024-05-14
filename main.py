from Ejercicio_2 import adivina, decorador_mensaje

@decorador_mensaje
def main():
    juego = adivina()
    juego()

if __name__ == "__main__":
    main()