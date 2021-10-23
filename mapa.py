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
        self.centroPantallaY = cantidadFilas // 2 # Se divide para obtener el centro de la matriz, que es 100x100 
        self.centroPantallaX = cantidadColumnas // 2
        self.maxNegativa = 0
        self.maxPositivaY = 90
        self.maxPositivaX = 80
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
        """SE crea el mapa con la amtriz y se le agrega si es montaña, agua o tierra"""
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
        """Se genera el spawn del personaje aleatoriamente en el centro de la pantalla"""
        numX = randint(30, 70)
        numY = randint(40, 60)
        while self.mapa[numY][numX].isSpawnable() != True:
            numX = randint(30, 70)
            numY = randint(40, 60) 
            
        self.descubirMapa(numY, numX, 4)
        return numY, numX



    def getCentroPantalla(self):
        return self.centroPantallaX, self.centroPantallaY
        

    def descubirMapa(self, posPersonajeY, posPersonajeX, visibilidad):
        """Se descubre el mapa a medida que el personaje avanza"""
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


    def set_centro_pantalla_y(self, numeroNuevoY):
        """Se setea el nuevo centro de la pantalla en el eje Y"""
        self.centroPantallaY =  self.centroPantallaY + numeroNuevoY
        if self.centroPantallaY <= self.maxNegativa:
            self.centroPantallaY = self.maxNegativa
        if self.centroPantallaY >= self.maxPositivaY:
            self.centroPantallaY = self.maxPositivaY
        print(self.centroPantallaY)
            
    def set_centro_pantalla_x(self, numeroNuevoX):
        """Se setea el nuevo centro de la pantalla en el eje X"""
        self.centroPantallaX = self.centroPantallaX + numeroNuevoX
        if self.centroPantallaX <= self.maxNegativa:
            self.centroPantallaX = self.maxNegativa
        if self.centroPantallaX >= self.maxPositivaX:
            self.centroPantallaX = self.maxPositivaX
        print(self.centroPantallaX) 
        
    def set_centro_pantalla_minimo_y(self, numeroNuevoMinimoY):
        self.centroPantallaY =  self.centroPantallaY + numeroNuevoMinimoY
        if self.centroPantallaY <= self.maxNegativa:
            self.centroPantallaY = self.maxNegativa
        print(self.centroPantallaY)

    def set_centro_pantalla_maximo_y(self, numeroNuevoMaximoY):
        self.centroPantallaY =  self.centroPantallaY + numeroNuevoMaximoY
        if self.centroPantallaY <= self.maxPositiva:
            self.centroPantallaY = self.maxPositiva
        print(self.centroPantallaY)

    def set_centro_pantalla_minimo_x(self, numeroNuevoMinimoX):
        self.centroPantallaX =  self.centroPantallaX + numeroNuevoMinimoX
        if self.centroPantallaX <= self.maxNegativa:
            self.centroPantallaX = self.maxNegativa
        print(self.centroPantallaX)

    def set_centro_pantalla_maximo_x(self, numeroNuevoMaximoX):
        self.centroPantallaX =  self.centroPantallaX + numeroNuevoMaximoX
        if self.centroPantallaX <= self.maxPositiva:
            self.centroPantallaX = self.maxPositiva
        print(self.centroPantallaX)
