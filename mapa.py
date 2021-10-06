from random import randint
import numpy as np
from celda import Celda

class Mapa():
    def __init__(self, cantidadFilas = 100, cantidadColumnas = 100) -> None:
        self.fila = 100
        self.col = 100
        #self.mapas =  np.random.randint(0, 100,(cantidadFilas,cantidadColumnas))
        self.mapaObjetos = np.random.randint(0, 100,(cantidadFilas, cantidadColumnas))
        self.mapaOculto = self.generarMapa(cantidadFilas, cantidadColumnas, False) #Le asigno un valor a cada posicion         
        #self.mapa = self.generarMapaAleatorio(cantidadFilas, cantidadColumnas)
    
    def generarMapaAleatorio(self):
        cantidadFilas = 100
        cantidadColumnas = 100
        mapas =  np.random.randint(0, 100,(cantidadFilas,cantidadColumnas))        

    def generarMapa(fil, col, val):
        """Crea una matriz con las filas y columnas y el valor q le vamos a pasar"""
        mapa = []
        for i in range(fil):
            mapa.append([])
            for j in range(col):
                mapa[i].append(Celda(val))
        return mapa    
        

    def getPosCelda(self):
        #posCelda = self.mapaOculto[y][x]
        pass
        

    def descubirMapa(self, posPersonajeY, posPersonajeX, visibilidad):
        for y in range((posPersonajeY + visibilidad), (posPersonajeY - visibilidad)):
            for x in range((posPersonajeX + visibilidad), (posPersonajeX - visibilidad)):
                if 0 < y < self.fila:
                    if 0 < x < self.col:
                        self.mapaObjetos[y][x].visibilizar()
   
