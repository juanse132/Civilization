from random import randint
import numpy as np
from celda import Celda

class Mapa():
    def __init__(self, cantidadFilas = 100, cantidadColumnas = 100) -> None:
        self.celda = Celda()
        self.mapas =  np.random.randint(0, 100,(cantidadFilas,cantidadColumnas))
        self.mapaObjetos = np.random.randint(0, 100,(cantidadFilas, cantidadColumnas))
        self.oculto = self.generarMapa(cantidadFilas, cantidadColumnas, False)        

    def generarMapaAleatorio(self):
        pass

    def generarMapa(fil, col, val):
        """Crea una matriz con las filas y columnas y el valor q le vamos a pasar"""
        mapa = []
        for i in range(fil):
            mapa.append([])
            for j in range(col):
                mapa[i].append(val)
        return mapa    
        
    def mostrarMapa(mapa):
        for fila in mapa:
            for elem in fila:
                print(elem, end = " ")
            print()

    def getPos(self):
        pass

    def descubirMapa(self):
        pass