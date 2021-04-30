# Minijuegos hechos por Hector Ivan Tyrpak

import paroimpar
import adivinaelnumero
import dados

class Minijuego:
    # Class attributes
    minijuego_dict = dict()
    minijuego_count = 0

    # Instance methods
    def __init__(self, nombre):
        self.nombre = nombre
        Minijuego.minijuego_count += 1
        Minijuego.minijuego_dict[Minijuego.minijuego_count] = self.nombre

    # Metodos Static
    @staticmethod
    def preguntar_minijuego():
        Minijuego.MinijuegoActual = input(
            f"\nElije el juego que quieres jugar. (Ingresa 0 para salir): ")
        try:
            Minijuego.MinijuegoActual = int(Minijuego.MinijuegoActual)
        except:
            pass
        
        if type(Minijuego.MinijuegoActual) != int: return Minijuego.preguntar_minijuego()
        elif any([Minijuego.MinijuegoActual > Minijuego.minijuego_count, 
                  Minijuego.MinijuegoActual <0]): return Minijuego.preguntar_minijuego()
        elif Minijuego.MinijuegoActual == 0: exit()
        
        # Opciones de minijuegos.
        elif Minijuego.MinijuegoActual == 1: paroimpar.ParOImpar.jugar_juego()
        elif Minijuego.MinijuegoActual == 2: adivinaelnumero.AdivinaElNumero.jugar_juego()
        elif Minijuego.MinijuegoActual == 3: dados.Dados.jugar_juego()

        Minijuego.imprime_minijuego_dict()
        Minijuego.preguntar_minijuego()

    @staticmethod
    def imprime_minijuego_dict():
        print(f"\nMinijuegos Disponibles:")
        for key, value in Minijuego.minijuego_dict.items():
            print(f"{key}. {value}")


# Instancias de minijuegos. Si se agrega un minijuego agregarlo aca.
mj1 = Minijuego("Par o Impar")
mj2 = Minijuego("Adivina el Numero")
mj3 = Minijuego("Dados")

print(f"\nBienvenido a los Minijuegos!",)

Minijuego.imprime_minijuego_dict()
Minijuego.preguntar_minijuego()