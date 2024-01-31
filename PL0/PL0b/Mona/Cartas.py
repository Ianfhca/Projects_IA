import random


class Carta(object):
    """Representa una carta en este caso de la baraja espanola
    
    Attributoss:
      palo: integer 0-3
      rango: integer 1-11
    """

    palo_nombres = ["Bastos", "Oros", "Copas", "Espadas"]
    rango_nombres = [None, "As", "2", "3", "4", "5", "6", "7", "Sota", "Caballo", "Rey"]

    def __init__(self, palo=0, rango=2):
        self.palo = palo
        self.rango = rango

    def __str__(self):
        """Devuelve la carta en modo legible."""
        return '%s de %s' % (Carta.rango_nombres[self.rango],
                             Carta.palo_nombres[self.palo])

    def __cmp__(self, other):
        """Compara una carta con otra
        Devuelve un positivo si self > other; negativo si other > self;
        y 0 si equivalentes.
        """
        #TOD Añadir el codigo para reescribir el cmp
        if self.rango > other.rango:
            rdo = 1
        elif self.rango < other.rango:
            rdo = -1
        else:
            rdo = 0
        return rdo

    """ def __eq__(self, other):
        rdo = False
        if isinstance(other, Carta):
            #TOD Añadir el codigo para reescribir el eq

            if Carta.__cmp__(self, other) == 0:
                if self.palo == 0 and other.palo == 3 or self.palo == 3 and other.palo == 0:
                    rdo = True
                elif self.palo == 1 and other.palo == 2 or self.palo == 2 and other.palo == 1:
                    rdo = True
        return rdo """
    
    def __eq__(self, other):
        return isinstance(other, Carta) and self.rango == other.rango and self.palo == other.palo

    """ def __lt__(self, other):
        return self.rango < other.rango or (self.rango == other.rango and self.palo < other.palo)

    def __le__(self, other):
        return self < other or self == other """

    def __ne__(self, other):
        """self != other"""
        eq = Carta.__eq__(self, other)
        return not eq


class Mazo(object):
    """Representa el mazo de cartas.
    Attributos:
      cartas: una lista de cartas que añadimos una a una.
    """
    
    def __init__(self):
        self.cartas = []
        for palo in range(4):
            for rango in range(1, 11):
                carta = Carta(palo, rango)
                self.cartas.append(carta)

    def __str__(self):
        res = []
        for carta in self.cartas:
            res.append(str(carta))
        return '\n'.join(res)


    def anadir_carta(self, carta):
        """Anade una carta al mazo."""
        self.cartas.append(carta)

    def eliminar_carta(self, carta):
        """Elimina una carta del mazo."""
        
        if carta in self.cartas:
            print("Se eliminó la carta: {0}".format(carta))
            self.cartas.remove(carta)
            rdo = True
        else:
            rdo = False
        return rdo

    def esta_carta(self, carta):
        """Comprueba si una carta está en el mazo.
        True si esta
        False sino"""
        if carta in self.cartas:
            rdo = True
        else:
            rdo = False
        return rdo
    
    def pop_carta(self, i=-1):
        """Saca una carta del mazo.
        i: el indice de la carta a sacar (por defecto -1, es decir, la ultima); 
        """
        return self.cartas.pop(i)

    def barajar(self):
        """Baraja las cartas del mazo."""
        random.shuffle(self.cartas)

    def ordenarAsc(self):
        """Ordena las cartas del mazo en orden ascendente."""
        self.cartas.sort(key = lambda x: x.rango )
        

    def mover_cartas(self, mano, num):
        """Mueve un numero num de cartas desde el mazo a la mano.
        mano: objeto destino perteneciente a la clase Mano
        num:  numero de cartas a desplazar
        """
        for i in range(num):
            #TOD Anadir el codigo que falta
            mano.anadir_carta(self.pop_carta(-1))

    def imprimir(self):
        for idx,carta in enumerate(self.cartas):
            print('  {0} - {1}'.format(idx,carta))

    def esta_vacio(self):
        """Devuelve True si esta vacio:  emplear len"""
        #TOD Anadir el codigo que falta
        return len(self.cartas) == 0

    def repartir_cartas(self, manos, num_cartas=999):
        num_manos = len(manos)
        i=0
        while i <= num_cartas and not self.esta_vacio():
            #TOD Anadir el codigo 
            carta = self.pop_carta()        # coger la carta de la cima
            mano = manos[i % num_manos]     # calcular a quien repartir
            mano.anadir_carta(carta)        # anadir una carta a una mano
            i+=1

class Mano(Mazo):
    """Representa una mano a jugar."""
    
    def __init__(self, jugador=''):
        self.cartas = []
        self.jugador = jugador

    
    def imprimir(self):
        """ Reescribir tal que indique el nombre del jugador propietario de esa mano
        asi como si esta vacia o de no estarlo las cartas que contiene:
        la mano de X esta vacia o la mano de X contiene bla bla.
        emplear el imprimir de la clase madre para imprimir la lista de cartas"""
        
        #TOD Anadir el codigo
        if (self.esta_vacio()):
            print("La mano de {0} está vacia".format(self.jugador))
        else:
            print("La mano de {0} es: ".format(self.jugador))
            super().imprimir()

class ManoPersona(Mano):
    ####################################
    # Forman pareja:
    # numX de bastos y numX de espadas
    # numX de copas  y numx de oros
    ####################################
    def eliminar_parejas(self):

        cont = 0

        salir = False #chivato para salir cuando la pareja que se pretende eliminar no sea tal

        while not salir:
            super().imprimir()
            print("Que cartas forman pareja? de 0 a {0}".format(len(self.cartas)-1))
            idxCarta,idxPareja = map(int, input().split(','))
            carta = self.cartas[idxCarta]
            posiblePareja = self.cartas[idxPareja]
            print(carta)
            print(posiblePareja)
            pareja = Carta(3 - carta.palo, carta.rango)#

            print(pareja)
            if posiblePareja == pareja: #TOD Anadir el codigo para comprobar si la que debiera ser pareja es la esperada y si fuese el caso eliminar ambas de la mano
                self.eliminar_carta(carta)
                self.eliminar_carta(posiblePareja)
                print("En la mano de {0} forman pareja el {1} y {2}".format(self.jugador, carta, posiblePareja))#pareja))
                cont += 1
            else:
                print("Las cartas {0} y {1} no son pareja".format(carta, posiblePareja))
                salir = True
                
        return cont

class ManoPC(Mano):
    ####################################
    # Forman pareja:
    # numX de bastos y numX de espadas
    # numX de copas  y numx de oros
    ####################################
    def eliminar_parejas(self):
        cont = 0# contador de cuantas parejas se eliminan
        originales_cartas = self.cartas[:]

        #TODO anadir el codigo para buscar y eliminar parejas AUTOMATICAMENTE

        for carta in self.cartas:
            pareja = Carta(3 - carta.palo, carta.rango)
            if self.esta_carta(pareja):
                print("Las cartas {0} y {1} son pareja".format(carta, pareja))
                self.eliminar_carta(carta)
                self.eliminar_carta(pareja)
                cont+=1
        super().imprimir()
        return cont
        


if __name__ == '__main__':
    #ejemplo1
    print("Ejemplo 1 mover cartas del mazo a una mano: ")
    mazo = Mazo()
    mazo.barajar()

    mano = Mano("Juan")
    mazo.mover_cartas(mano, 5)
    mano.ordenarAsc()
    mano.imprimir()

    print("\n\n Ejemplo 2 repartir cartas entre 3 jugadores (9 cartas): ")
    mazo = Mazo()
    mano1 = ManoPersona('Jug_1')
    mano2 = ManoPersona('Jug_2')
    mano3 =ManoPersona('Jug_3')
    mazo.repartir_cartas([mano1,mano2,mano3],9)
    mano1.imprimir()
    mano2.imprimir()
    mano3.imprimir()

    
    

    
