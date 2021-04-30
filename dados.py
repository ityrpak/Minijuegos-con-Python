# Juego de Dados por Hector Ivan Tyrpak

# Posible ampliacion: IA para la computadora

import random

class Dados:

    def __init__(self, nombre):
        self.__nombre = nombre
        self.__dados_a_tirar = 6
        self.__puntos_ronda = 0
        self.__puntos_acumulados = 0
        self.__ronda = 1
        self.__mano_actual = []
        self.__estado_farkle = False


    def nombre_setter(self, nombre):
        self.__nombre = nombre

    def nombre_getter(self):
        return self.__nombre


    def dados_a_tirar_setter(self, int):
        self.__dados_a_tirar = int

    def dados_a_tirar_getter(self):
        return self.__dados_a_tirar

    def dados_a_tirar_resta(self, int):
        self.__dados_a_tirar -= int


    def puntos_ronda_setter(self, int):
        self.__puntos_ronda = int

    def puntos_ronda_getter(self):
        return self.__puntos_ronda

    def puntos_ronda_suma(self, int):
        self.__puntos_ronda += int


    def puntos_acumulados_setter(self, int):
        self.__puntos_acumulados = int

    def puntos_acumulados_getter(self):
        return self.__puntos_acumulados

    def puntos_acumulados_suma(self, int):
        self.__puntos_acumulados += int


    def ronda_setter(self, int):
        self.__ronda = int

    def ronda_getter(self):
        return self.__ronda

    def ronda_suma(self):
        self.__ronda +=1


    def mano_actual_setter(self, list):
        self.__mano_actual = list

    def mano_actual_getter(self):
        return self.__mano_actual

    def mano_actual_item_getter(self, i):
        return self.__mano_actual[i]

    def mano_actual_append(self):
        self.__mano_actual.append(random.randint(1,6))

    def mano_actual_sorter(self):
        self.__mano_actual.sort()

    def mano_actual_count(self, int):
        return self.__mano_actual.count(int)


    def estado_farkle_getter(self):
        return self.__estado_farkle

    def estado_farkle_true(self):
        self.__estado_farkle = True

    def estado_farkle_false(self):
        self.__estado_farkle = False



    # Metodos
    def pregunta_retirar(self):
        print(f"\nRonda {p1.ronda_getter()}. Puntos en la ronda: {p1.puntos_ronda_getter()}. Puntos acumulados: {p1.puntos_acumulados_getter()} Dados a tirar: {p1.dados_a_tirar_getter()}")
        respuesta = input(f"\nQueres volver a tirar? (presiona 1 para si, otra tecla para no) ")
        if respuesta == "1": self.tirar()
        else: 
            p1.puntos_acumulados_suma(p1.puntos_ronda_getter())
            if p1.puntos_acumulados_getter() >= 5000:
                self.victoria_jugador()
            else:
                p1.puntos_ronda_setter(0)
                print(f"\nFin de la Ronda {p1.ronda_getter()}. Puntos actuales: {p1.puntos_acumulados_getter()}.")
                p1.puntos_ronda_setter(0)
                p1.dados_a_tirar_setter(6)
                p1.ronda_suma()
                self.tirar()

    def resetear_dados(self):
        p1.mano_actual_setter([])

    def victoria_jugador(self):
        print(f"JUEGO TERMINADO! Felicitaciones {p1.nombre_getter()}, ganaste en {p1.ronda_getter()} rondas con {p1.puntos_acumulados_getter()} puntos!")
        Dados.pregunta_jugar_denuevo()

    def tirar(self):
        self.resetear_dados()
        p1.estado_farkle_false()
        if p1.dados_a_tirar_getter() == 0: p1.dados_a_tirar_setter(6)
        for i in range(p1.dados_a_tirar_getter()):
            p1.mano_actual_append()
        p1.mano_actual_sorter()
        print(f"\nMano:")
        for i in range(len(p1.mano_actual_getter())): print(f"Dado Nº{i+1}: {p1.mano_actual_item_getter(i)}")
        self.recuento_dados()

    def recuento_dados(self):
        if p1.mano_actual_getter() == [1, 1, 1, 1, 1, 1]: self.victoria_jugador()
        while True:
            if self.verificar_escalera(): break
            if self.verificar_x_dados(): break
            elif self.tantos_dados:
                self.verificar_unos_cincos()
                break
            if self.verificar_3_pares(): break
            if self.verificar_triples(): break
            if self.verificar_unos_cincos(): break
            else: 
                self.farkle()
                break
        if p1.estado_farkle_getter() == True: return p1.tirar()
        else: self.pregunta_retirar()

    def verificar_escalera(self):
        if p1.mano_actual_getter() == [1, 2, 3, 4, 5, 6]:
            p1.puntos_ronda_suma(1500)
            print(f"\nESCALERA!")
            self.resetear_dados()
            return True

    def verificar_x_dados(self):
        self.tantos_dados = False
        for n in range(1,7):
            for count in [6, 5, 4]:
                if p1.mano_actual_count(n) == count:
                    print(f"\n{count} en una mano!")
                    self.tantos_dados = True
                    p1.puntos_ronda_suma(1000*count - 3000)
                    p1.dados_a_tirar_resta(count)
                    self.triples = True
                    if count == 6: return True

    def verificar_3_pares(self):
        if p1.dados_a_tirar_getter() != 6: return
        if (p1.mano_actual_item_getter(0) == p1.mano_actual_item_getter(1) and p1.mano_actual_item_getter(2)
        == p1.mano_actual_item_getter(3) and p1.mano_actual_item_getter(4) == p1.mano_actual_item_getter(5)):
            print(f"\nTres pares!")
            p1.puntos_ronda_suma(1500)
            return True

    def verificar_triples(self):
        self.triples = 0
        for n in range(1,7):
            if p1.mano_actual_count(n) == 3:
                self.triples += 1
                if n != 1: p1.puntos_ronda_suma(n*100)
                else: p1.puntos_ronda_suma(1000)
                for i in range(len(p1.mano_actual_getter())):
                    if p1.mano_actual_item_getter(i) == n:
                        p1.dados_a_tirar_resta(1)
        else:
            if self.triples == 2:
                print(f"\nDos triples!")
                p1.dados_a_tirar_setter(6)
                p1.puntos_ronda_suma(2500)
                return True

    def verificar_unos_cincos(self):
        self.unos_cincos = False
        if self.triples > 0: self.unos_cincos = True
        conteo_cincos = p1.mano_actual_count(5)
        conteo_unos = p1.mano_actual_count(1)
        if conteo_cincos <= 2 and conteo_cincos != 0:
            p1.puntos_ronda_suma(50*conteo_cincos)
            p1.dados_a_tirar_resta(conteo_cincos)
            # p1.puntos_acumulados_suma(p1.puntos_ronda_getter())
            self.unos_cincos = True
        if conteo_unos <= 2 and conteo_unos != 0:
            p1.puntos_ronda_suma(100*conteo_unos)
            p1.dados_a_tirar_resta(conteo_unos)
            # p1.puntos_acumulados_suma(p1.puntos_ronda_getter())
            self.unos_cincos = True
        if p1.dados_a_tirar_getter() == 0: p1.dados_a_tirar_setter(6)
        return self.unos_cincos

    def farkle(self):
        print(f"\nFarlke! Perdiste todos los puntos de esta ronda.")
        input()
        p1.estado_farkle_true()
        p1.dados_a_tirar_setter(6)
        p1.puntos_ronda_setter(0)
        p1.ronda_suma()

    # Metodos Static
    @staticmethod
    def preguntar_reglas():
        if input(f"{p1.nombre_getter()} bienvenido a Dados! Presiona 1 para leer las reglas. Si no, presiona enter \n") == "1":
            print("""Cada jugador tirará 6 dados. Cualquier dado que
anote puntos son separados. Entonces el jugador tiene dos
opciones:

1) El puede terminar su turno anotando los puntos de la
ronda para su puntaje total o
2) El puede volver a tirar con los dados remanentes (los
dados que no tenian puntos). Si uno o mas dados de su
segunda mano, los separara tal como hizo en la primer
mano y los puntos se sumaran a los puntos de la ronda.

Pero si en una tirada ningun dado suma puntos, se declarara
Farkle! y el jugador perdera todos los puntos de la ronda
acumulados.

Tabla de puntos:

5's = 50 pts
1's = 100 pts
3 x 2's = 200 pts
3 x 3's = 300 pts
3 x 4's = 400 pts
3 x 5's = 500 pts
3 x 6's = 600 pts
3 x 1's = 1000 pts

4 dados iguales = 1000 pts
5 dados iguales = 2000 pts
6 dados iguales = 3000 pts
Escalera 1 a 6 = 1500 pts

3 pares = 1500
2 triples = 2500

4 y 2 iguales = 1500 pts
Para ganar, hay que acumular 5000 puntos.
""")
            input("Presiona una tecla para continuar")


    @staticmethod
    def jugar_juego():

        n = input("Introduce tu nombre: ")
        global p1 
        p1 = Dados(n)
        Dados.preguntar_reglas()
        p1.resetear_dados()
        p1.ronda_setter(1)
        p1.tirar()

    @staticmethod
    def pregunta_jugar_denuevo():
        respuesta = input(f"\nPresiona 1 para jugar de nuevo. Presiona cualquier tecla para regresar al menu. ")
        if respuesta == "1": return Dados.jugar_juego()
        else: return