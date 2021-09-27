from celda import Celda
import pygame
from sys import exit
from pygame import time
from random import randint
import numpy as np
from pygame.constants import MOUSEBUTTONDOWN
from tierra import Tierra
from water import Agua
from montaña import Montaña


class mapacheto:
    def __init__(self, cantidadFilas = 60, cantidadColumnas = 60, tamañoCelda = 20):
        pygame.init()
        anchoPantalla = 800
        largoPantalla = 400
        self.screen = pygame.display.set_mode((anchoPantalla,largoPantalla))
        pygame.display.set_caption('Civilization')
        self.fotoTierra = Tierra()
        self.fotoAgua = Agua()
        self.fotoMontaña = Montaña()
        self.tamañoCelda = tamañoCelda
        self.celdasPantallaTotalHorizontal = anchoPantalla // self.tamañoCelda #40 
        self.celdasPantallaTotalVertical = largoPantalla // self.tamañoCelda #20
        self.centroPantallaX = cantidadFilas // 2 # Se divide para obtener el centro de la matriz, que es 60x60 
        self.centroPantallaY = cantidadColumnas // 2
        self.posicionPersonajeX =  self.centroPantallaX
        self.posicionPersonajeY =  self.centroPantallaY
        self.mapa =  np.random.randint(0, 100,(cantidadFilas,cantidadColumnas))
        self.mapaObjetos = np.random.randint(0, 100,(cantidadFilas, cantidadColumnas))

        self.fondoAgua = self.fotoAgua.cargar_agua()
        self.fondoMont = self.fotoMontaña.cargar_montaña()
        self.fondoTier = self.fotoTierra.cargar_tierra()
        self.arbol = self.cargar_foto('imagenes/arbolrefull.png')
        self.hombre = self.cargar_foto('Tropas y personajes/3 Man/Man.png')
        self.manWalk = self.cargar_foto('Tropas y personajes/3 Man/Man_Walk.png')
        self.mapaObjetos[self.posicionPersonajeY][self.posicionPersonajeX] = -1


    def movimiento_pantalla(self, key):
        """Me muevo por la pantalla hasta los limites de la matriz"""
        maxNegativa = 0
        maxPositiva = 30    
        if key == pygame.K_UP:
            self.centroPantallaY -= 2
            if self.centroPantallaY <= maxNegativa:
                self.centroPantallaY = maxNegativa
        if key == pygame.K_DOWN:
            self.centroPantallaY += 2
            if self.centroPantallaY >= maxPositiva:
                self.centroPantallaY = maxPositiva
        if key == pygame.K_LEFT:
            self.centroPantallaX -= 2
            if self.centroPantallaX <= maxNegativa:
                self.centroPantallaX = maxNegativa
        if key == pygame.K_RIGHT:
            self.centroPantallaX += 2
            if self.centroPantallaX >= maxPositiva:
                self.centroPantallaX = maxPositiva

    def mover_personaje(self):
        """Genero el moviemiento del personaje haciendo clicks"""
        self.mapaObjetos[self.posicionPersonajeY][self.posicionPersonajeX] = 0
        mousePosX, mousePosY = pygame.mouse.get_pos()
        posXCeldas = (mousePosX//self.tamañoCelda) # Lo escala al tamaño de las celdas
        posYCeldas = (mousePosY//self.tamañoCelda) 
        self.posicionPersonajeX = posXCeldas + self.centroPantallaX - (self.celdasPantallaTotalHorizontal//2) 
        self.posicionPersonajeY = posYCeldas + self.centroPantallaY - (self.celdasPantallaTotalVertical//2) 
        self.mapaObjetos[self.posicionPersonajeY][self.posicionPersonajeX] = -1

    def cargar_foto(self, imagen):
        """Cargo todas las fotos y las escalo al tamaño de las celdas de la matriz"""
        fotoOriginal = pygame.image.load(imagen)
        fotoEscalada = pygame.transform.scale(fotoOriginal, (self.tamañoCelda, self.tamañoCelda))
        return (fotoEscalada)

    def mostrar_mapa(self):
        """Recorro ambas matrizes y cargo el mapa"""
        forY = 0

        for y in range(self.centroPantallaY - (self.celdasPantallaTotalVertical//2), self.centroPantallaY + (self.celdasPantallaTotalVertical//2)):
            forX = 0
            for x in range(self.centroPantallaX - (self.celdasPantallaTotalHorizontal // 2), self.centroPantallaX + (self.celdasPantallaTotalHorizontal // 2)):
                
                fondo = self.mapa[y][x]
                fondoObjetos = self.mapaObjetos[y][x]
                
                if 0 <= fondo <= 1:
                    fondoADibujar = self.fondoAgua
                elif 2 <= fondo <= 4:
                    fondoADibujar = self.fondoMont
                elif 5 <= fondo <= 100:
                    fondoADibujar = self.fondoTier

                self.screen.blit(fondoADibujar, (forX * self.tamañoCelda, forY * self.tamañoCelda)) 

                if 5 <= fondo <= 15:
                    self.screen.blit(self.arbol, (forX * self.tamañoCelda, forY * self.tamañoCelda)) 

                if fondoObjetos == -1:
                    if 16 <= fondo <= 100:
                        self.screen.blit(self.hombre, (forX * self.tamañoCelda, forY * self.tamañoCelda))
                    else:
                        pass # Hacer que se printe en la ultima posicion el hombre y que no no aparezca directamente

                forX += 1

            forY += 1
