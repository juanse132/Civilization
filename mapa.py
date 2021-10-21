from random import randint
import numpy as np
from celda import Celda
from montaña import Montaña
from tierra import Tierra
from water import Agua
from personaje import Personaje



class Mapa():
    def __init__(self, cantidadFilas = 100, cantidadColumnas = 100) -> None:
        self.fila = 100
        self.col = 100
        self.centroPantallaX = cantidadFilas // 2 # Se divide para obtener el centro de la matriz, que es 60x60 
        self.centroPantallaY = cantidadColumnas // 2
        self.maxNegativa = 0
        self.maxPositiva = 100
#        self.recurso = self.generar_matriz_sprite()
        self.mapa = self.generarMapa(cantidadFilas, cantidadColumnas, True) #Le asigno un valor a cada posicion 
       # self.mapa_recursos = self.generar_mapa_recursos()
        # TODO: cambiar último argumento a False        
        #self.mapa = self.generarMapaAleatorio(cantidadFilas, cantidadColumnas)
        #self.mapas =  np.random.randint(0, 100,(cantidadFilas,cantidadColumnas))
        #self.mapaObjetos = np.random.randint(0, 100,(cantidadFilas, cantidadColumnas))
        self.personaje = Personaje(self.playerSpawn())
    
    def generarMapaAleatorio(self):
        cantidadFilas = 100
        cantidadColumnas = 100
        mapas =  np.random.randint(0, 100,(cantidadFilas,cantidadColumnas))        

    def generarMapa(self, fil, col, val):
        """Crea una matriz con las filas y columnas y el valor q le vamos a pasar"""
        mapa = []
        tipos = [Montaña, Agua, Tierra]
        for i in range(fil):
            mapa.append([])
            for j in range(col):
                num = randint(0,100)
                if num<5:
                    tipo = tipos[0]
                elif num>95:
                    tipo = tipos[1]
                else:
                    tipo = tipos[2]

                mapa[i].append(tipo())
                
        return mapa
            

    def get_mapa_recursos(self):
        return self.mapa_recursos

    def get_mapa(self):
        return self.mapa
    

    def playerSpawn(self):
        from jugar import Juego
        controlador = Juego
        #Todo: falta arreglar lo del personaje en cuanto al controlador
        anchoMinimoPantalla, anchoMaximoPantalla = controlador.get_ancho_pantalla()
        largoMinimoPantalla, largoMaximoPantalla = controlador.get_largo_pantalla()
        numX = randint(largoMinimoPantalla,largoMinimoPantalla)
        numY = randint(anchoMinimoPantalla,anchoMaximoPantalla)
        while self.mapa[numY][numX].isSpawnable() != True:
            numX = randint(largoMinimoPantalla,largoMaximoPantalla)
            numY = randint(anchoMinimoPantalla,anchoMaximoPantalla)
            
        self.descubirMapa(numY, numX, 4)
        return numY, numX



    def getCentroPantalla(self):
        return self.centroPantallaX, self.centroPantallaY
        

    def descubirMapa(self, posPersonajeY, posPersonajeX, visibilidad):
        for y in range((posPersonajeY + visibilidad), (posPersonajeY - visibilidad)):
            for x in range((posPersonajeX + visibilidad), (posPersonajeX - visibilidad)):
                if 0 < y < self.fila:
                    if 0 < x < self.col:
                        self.mapa[y][x].visibilizar()
   

    def get_recurso(self):
        return self.recurso
    
    def get_item(self, y, x):
        return self.mapa[y][x]

    def get_personaje(self):
        return self.personaje


    def set_centro_pantalla_y(self, numeroNuevo):
        self.centroPantallaY =  self.centroPantallaY + numeroNuevo
        if self.centroPantallaY <= self.maxNegativa:
            self.centroPantallaY = self.maxNegativa
        if self.centroPantallaY >= self.maxPositiva:
            self.centroPantallaY = self.maxPositiva


    def set_centro_pantalla_x(self, numeroNuevo):
        self.centroPantallaX = self.centroPantallaX + numeroNuevo
        if self.centroPantallaX <= self.maxNegativa:
            self.centroPantallaX = self.maxNegativa
        if self.centroPantallaX >= self.maxPositiva:
            self.centroPantallaX = self.maxPositiva 
