from random import randint
import numpy as np
from celda import Celda
from montaña import Montaña
from tierra import Tierra
from water import Agua

class Mapa():
    def __init__(self, cantidadFilas = 100, cantidadColumnas = 100) -> None:
        self.fila = 100
        self.col = 100
        self.mapa = []
        self.centroPantallaX = cantidadFilas // 2 # Se divide para obtener el centro de la matriz, que es 60x60 
        self.centroPantallaY = cantidadColumnas // 2
        #self.mapas =  np.random.randint(0, 100,(cantidadFilas,cantidadColumnas))
        #self.mapaObjetos = np.random.randint(0, 100,(cantidadFilas, cantidadColumnas))
        self.mapaOculto = self.generarMapa(cantidadFilas, cantidadColumnas, True) #Le asigno un valor a cada posicion         
        #self.mapa = self.generarMapaAleatorio(cantidadFilas, cantidadColumnas)
    
    def generarMapaAleatorio(self):
        cantidadFilas = 100
        cantidadColumnas = 100
        mapas =  np.random.randint(0, 100,(cantidadFilas,cantidadColumnas))        

    def generarMapa(self, fil, col, val):
        """Crea una matriz con las filas y columnas y el valor q le vamos a pasar"""
        for i in range(fil):
            self.mapa.append([])
            for j in range(col):
                #tipos = ["montaña", "agua", "tierra"]
                tipos = [Montaña, Agua, Tierra]
                num = randint(0,2)
                self.mapa[i].append(tipos[num]())
                

        return self.mapa    
        
    def playerSpawn(self):
        numX = randint(0,80)
        numY = randint(0,80)
        while self.mapaOculto[numY][numX].isSpawnable() != True:
            numX = randint(0,80)
            numY = randint(0,80)
            
        self.descubirMapa(numY, numX, 4)
        return numY, numX



    def getCentroPantalla(self):
        return self.centroPantallaX, self.centroPantallaY
        

    def descubirMapa(self, posPersonajeY, posPersonajeX, visibilidad):
        for y in range((posPersonajeY + visibilidad), (posPersonajeY - visibilidad)):
            for x in range((posPersonajeX + visibilidad), (posPersonajeX - visibilidad)):
                if 0 < y < self.fila:
                    if 0 < x < self.col:
                        self.mapaOculto[y][x].visibilizar()
   
