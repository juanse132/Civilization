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
        self.centroPantallaX = cantidadFilas // 2 # Se divide para obtener el centro de la matriz, que es 60x60 
        self.centroPantallaY = cantidadColumnas // 2
#        self.recurso = self.generar_matriz_sprite()
        self.mapa = self.generarMapa(cantidadFilas, cantidadColumnas, True) #Le asigno un valor a cada posicion 
       # self.mapa_recursos = self.generar_mapa_recursos()
        # TODO: cambiar último argumento a False        
        #self.mapa = self.generarMapaAleatorio(cantidadFilas, cantidadColumnas)
        #self.mapas =  np.random.randint(0, 100,(cantidadFilas,cantidadColumnas))
        #self.mapaObjetos = np.random.randint(0, 100,(cantidadFilas, cantidadColumnas))
        
    
    def generarMapaAleatorio(self):
        cantidadFilas = 100
        cantidadColumnas = 100
        mapas =  np.random.randint(0, 100,(cantidadFilas,cantidadColumnas))        

    def generarMapa(self, fil, col, val):
        """Crea una matriz con las filas y columnas y el valor q le vamos a pasar"""
        mapa = []
        tipos = [Montaña, Agua, Tierra]
        recursos = []
        for i in range(fil):
            mapa.append([])
            for j in range(col):
                #tipos = ["montaña", "agua", "tierra"]
                num = randint(0,100)
                if num<5:
                    tipo = tipos[0]
                elif num>95:
                    tipo = tipos[1]
                else:
                    tipo = tipos[2]

                mapa[i].append(tipo())
                
        return mapa
            

    # def generar_mapa_recursos(self):
    #     mapa_rec = []
    #     for i in range(100):
    #         mapa_rec.append([])
    #         for j in range(100):
    #             if self.mapa[i][j] == :
    #                 mapa_rec[i][j] = self.mapa[i][j]

    #     return mapa_rec

    def get_mapa_recursos(self):
        return self.mapa_recursos

    def get_mapa(self):
        return self.mapa
    
    # def generar_matriz_sprite(self):
    #     mapa_num = []
    #     for y in range(0, 100):
    #         mapa_num.append([])
    #         for x in range (0,100):
                
    #             self.mapa[y][x]



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
   

    def get_recurso(self):
        return self.recurso
    
    def get_item(self, y, x):
        return self.mapa[y][x]