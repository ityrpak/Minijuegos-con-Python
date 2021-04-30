# Guess the Number module by Enginikts

import random

class AdivinaElNumero:
    #Atributos de Clase
    numero = int()

    @staticmethod
    def input_jugador():
        try:
            AdivinaElNumero.numero = int(input("Ingresa un numero de 0 - 20: "))
            return AdivinaElNumero.numero
        except:
            AdivinaElNumero.input_jugador()

    @staticmethod
    def jugar_juego():
        print(f"\nAdivina el numero")
        x = random.randint(0,20)
        AdivinaElNumero.input_jugador()
        while AdivinaElNumero.numero != x: 
            if AdivinaElNumero.numero < x: print(f"Intenta con un numero mas alto.\n")
            else: print(f"Intenta con un numero mas bajo.\n")
            AdivinaElNumero.input_jugador()
        else:
            print(f"\nCorrecto!")    
        if AdivinaElNumero.pregunta_jugar_denuevo(): AdivinaElNumero.jugar_juego()
    
    @staticmethod
    def pregunta_jugar_denuevo():
        answer = input(f"\nPresiona 1 para jugar de nuevo. Presiona cualquier tecla para regresar al menu.")
        if answer == "1": return True