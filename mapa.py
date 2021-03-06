from random import randint
import numpy as np
from celda import Celda
from montaña import Montaña
from tierra import Tierra
from water import Agua
from personaje import Personaje
from guerrero_comun import Guerrero_comun
from aldeana import Aldeana
from aldeano import Aldeano

class Mapa():
    def __init__(self, celdastotalesXPantalla = 40, celdastotalesYPantalla = 20 ,cantidadFilas = 100, cantidadColumnas = 100) -> None:
        self.centroMapaY = cantidadFilas // 2 # Se divide para obtener el centro de la matriz, que es 100x100 
        self.centroMapaX = cantidadColumnas // 2
        self.maximo_minimo_pantalla()
        self.mapa = self.generarMapa(cantidadFilas, cantidadColumnas, False) # Le asigno un valor a cada posicion 
        self.personaje = self.crear_personaje(Aldeano, celdastotalesXPantalla, celdastotalesYPantalla)
        self.guerrero = self.crear_personaje(Guerrero_comun, celdastotalesXPantalla, celdastotalesYPantalla)
        self.aldeana = self.crear_personaje(Aldeana, celdastotalesXPantalla, celdastotalesYPantalla)

    def crear_personaje(self, personaje_clase, celdastotalesXPantalla, celdastotalesYPantalla): 
        """Creo un personaje con una posicion aleatoria en el mapa, de preferencia es centrado en la pantalla que ve el usuario"""
        spawn = self.playerSpawn(celdastotalesXPantalla, celdastotalesYPantalla)
        personaje = personaje_clase(spawn)
        self.mapa[spawn[0]][spawn[1]].set_personaje(personaje) # Cargo un personaje con esa posicion en el mapa  
        return personaje

    def maximo_minimo_pantalla(self):
        """Establezco los limites para no pasarme a la hora de mover la camara"""
        self.maxPositivaY = 90
        self.minNegativoY = 10

        self.maxPositivaX = 80
        self.minNegativoX = 20
    

    def generarMapa(self, fil, col, val):
        """SE crea el mapa con la amtriz y se le agrega si es montaña, agua o tierra"""
        mapa = []
        tipos = [Montaña, Agua, Tierra]
        for i in range(fil):
            mapa.append([])
            for j in range(col):
                num = randint(0,100)
                if num<8:
                    tipo = tipos[0]
                elif num>97:
                    tipo = tipos[1]
                else:
                    tipo = tipos[2]

                mapa[i].append(tipo())
        return mapa
            

    def get_mapa(self):
        return self.mapa


    def playerSpawn(self, celdasPantallaTotalHorizontal, celdasPantallaTotalVertical):
        """Se genera el spawn del personaje aleatoriamente en el centro de la pantalla"""
        yMinimaPantalla = ((self.centroMapaY - 10) + (celdasPantallaTotalVertical // 2)) + 2
        yMaximaPantalla = ((self.centroMapaY - 10)  + (celdasPantallaTotalVertical // 2)) - 2

        
        xMinimaPantalla =  ((self.centroMapaX - 20)  + (celdasPantallaTotalHorizontal // 2)) + 2
        xMaximoPantalla =  ((self.centroMapaX - 20) + (celdasPantallaTotalHorizontal // 2)) - 2

        
        numX = randint(xMaximoPantalla , xMinimaPantalla)
        numY = randint(yMaximaPantalla, yMinimaPantalla)
        while self.mapa[numY][numX].isSpawnable() != True:
            numX = randint(xMaximoPantalla , xMinimaPantalla)
            numY = randint(yMaximaPantalla, yMinimaPantalla) 
            
        self.descubirMapa(numY, numX, 4)
        return numY, numX


    def getCentroMapa(self):
        return self.centroMapaX, self.centroMapaY
        

    def descubirMapa(self, posPersonajeY, posPersonajeX, visibilidad):
        """Se descubre el mapa a medida que el personaje avanza"""
        for y in range((posPersonajeY + visibilidad), (posPersonajeY - visibilidad)):
            for x in range((posPersonajeX + visibilidad), (posPersonajeX - visibilidad)):
                if 0 < y < self.centroMapaY:
                    if 0 < x < self.centroMapaX:
                        self.mapa[y][x].visibilizar()
   
    
    def get_celda(self, y, x):
        return self.mapa[y][x]

    def get_personaje_inicial(self):
        return self.personaje

    def set_centro_pantalla_y(self, numeroNuevoY):
        """Se setea el nuevo centro de la pantalla en el eje Y"""
        self.centroMapaY =  self.centroMapaY + numeroNuevoY
        if self.centroMapaY <= self.minNegativoY:
            self.centroMapaY = self.minNegativoY
        if self.centroMapaY >= self.maxPositivaY:
            self.centroMapaY = self.maxPositivaY
            
    def set_centro_pantalla_x(self, numeroNuevoX):
        """Se setea el nuevo centro de la pantalla en el eje X"""
        self.centroMapaX = self.centroMapaX + numeroNuevoX
        if self.centroMapaX <= self.minNegativoX:
            self.centroMapaX = self.minNegativoX
        if self.centroMapaX >= self.maxPositivaX:
            self.centroMapaX = self.maxPositivaX 
