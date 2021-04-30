# Minijuego Par o Impar

class ParOImpar:

    @staticmethod
    def jugar_juego():
        print(f"\nPar o Impar")
        try:
            x = float(input("Ingresa un Numero: "))
        except:
            ParOImpar.jugar_juego()
        if x % 2 == 0: print("Es un numero par.")
        else: print("Es un numero impar.")
        if ParOImpar.pregunta_jugar_denuevo(): ParOImpar.jugar_juego()
    
    @staticmethod
    def pregunta_jugar_denuevo():
        answer = input(f"\nPresiona 1 para jugar de nuevo. Presiona cualquier tecla para regresar al menu.")
        if answer == "1": return True