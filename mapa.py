from random import randint
import numpy as np
from celda import Celda
from montaña import Montaña
from tierra import Tierra
from water import Agua
from personaje import Personaje



class Mapa():
    def __init__(self, celdastotaleXPantalla = 40, celdastotalesYPantalla = 20 ,cantidadFilas = 100, cantidadColumnas = 100) -> None:
        self.centroPantallaY = cantidadFilas // 2 # Se divide para obtener el centro de la matriz, que es 100x100 
        self.centroPantallaX = cantidadColumnas // 2
        
        self.maxPositivaY = 90
        self.minNegativoY = 20

        self.maxPositivaX = 80
        self.minNegativoX = 10

        self.mapa = self.generarMapa(cantidadFilas, cantidadColumnas, False) #Le asigno un valor a cada posicion         
        self.personaje = Personaje(self.playerSpawn(celdastotaleXPantalla, celdastotalesYPantalla))
    
    def generar_mapa_no_aleatorio(self):
        cantidadFilas = 100
        cantidadColumnas = 100
        mapas =  np.random.randint(0, 100,(cantidadFilas,cantidadColumnas))    
        #TODO:ver lo de generar 2 mapas     

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
                elif num>98:
                    tipo = tipos[1]
                else:
                    tipo = tipos[2]

                mapa[i].append(tipo())
        return mapa
            

    def get_mapa_recursos(self):
        return self.mapa_recursos

    def get_mapa(self):
        return self.mapa
    

    def playerSpawn2(self):
        """Se genera el spawn del personaje aleatoriamente en el centro de la pantalla"""
        numX = randint((self.centroPantallaX + 30) - 5 , ((self.centroPantallaX + 50) - 30) + 5)
        numY = randint((self.centroPantallaY + 20) - 5, ((self.centroPantallaY + 30) - 20) + 5)
        while self.mapa[numY][numX].isSpawnable() != True: 
            if self.mapa[numY][numX].isSpawnableRecurso() != True:
                numX = randint((self.centroPantallaX + 30) - 5, ((self.centroPantallaX + 50) - 30) + 5)
                numY = randint((self.centroPantallaY + 20) - 5, ((self.centroPantallaY + 30) - 20) + 5) 
            else:
                continue
            
        self.descubirMapa(numY, numX, 4)
        print (numY, numX)
        return numY, numX



    def playerSpawn(self, celdasPantallaTotalHorizontal, celdasPantallaTotalVertical):
        """Se genera el spawn del personaje aleatoriamente en el centro de la pantalla"""
        yMinimaPantalla = (celdasPantallaTotalVertical // 2) - 5
        yMaximaPantalla = (celdasPantallaTotalVertical // 2) + 5

        xMinimaPantala = (celdasPantallaTotalHorizontal // 2) - 5
        xMaximoPantala = (celdasPantallaTotalHorizontal // 2) + 5

        numX = randint(xMinimaPantala , xMaximoPantala)
        numY = randint(yMinimaPantalla, yMaximaPantalla)
        while self.mapa[numY][numX].isSpawnable() != True or self.mapa[numY][numX].isSpawnableRecurso() != True: 
            numX = randint(xMinimaPantala, xMaximoPantala)
            numY = randint(yMinimaPantalla, yMaximaPantalla) 
            # TODO: arreglar el problema del spawn
        
            
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
        if self.centroPantallaY <= self.minNegativoY:
            self.centroPantallaY = self.minNegativoY
        if self.centroPantallaY >= self.maxPositivaY:
            self.centroPantallaY = self.maxPositivaY
        print(self.centroPantallaY)
            
    def set_centro_pantalla_x(self, numeroNuevoX):
        """Se setea el nuevo centro de la pantalla en el eje X"""
        self.centroPantallaX = self.centroPantallaX + numeroNuevoX
        if self.centroPantallaX <= self.minNegativoX:
            self.centroPantallaX = self.minNegativoX
        if self.centroPantallaX >= self.maxPositivaX:
            self.centroPantallaX = self.maxPositivaX 
        print(self.centroPantallaX)
        