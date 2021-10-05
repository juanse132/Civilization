from random import randint
import numpy as np

class Mapa():
    def __init__(self, cantidadFilas = 100, cantidadColumnas = 100) -> None:
        #self.mapas =  np.random.randint(0, 100,(cantidadFilas,cantidadColumnas))
        self.mapaObjetos = np.random.randint(0, 100,(cantidadFilas, cantidadColumnas))
        self.oculto = self.generarMapa(cantidadFilas, cantidadColumnas, False) #Le asigno un valor a cada posicion         

    def generarMapaAleatorio():
        cantidadFilas = 100
        cantidadColumnas = 100
        mapas =  np.random.randint(0, 100,(cantidadFilas,cantidadColumnas))
        return mapas

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

    def getPosCelda(self):
        pass

    def descubirMapa(self):
        pass


    
