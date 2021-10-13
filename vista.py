import pygame
from sys import exit
from pygame import time
from random import randint
import numpy as np
from mapa import Mapa
from pygame.constants import MOUSEBUTTONDOWN
from tierra import Tierra
from water import Agua
from montaña import Montaña
from arbol import Arbol


class Vista:
    def __init__(self) -> None:
        pygame.init()
        anchoPantalla = 800
        largoPantalla = 400
        self.screen = pygame.display.set_mode((anchoPantalla,largoPantalla))
        pygame.display.set_caption('Civilization')
        self.tamañoFotoCelda = 20
        self.celdasPantallaTotalHorizontal = anchoPantalla // self.tamañoFotoCelda #40 
        self.celdasPantallaTotalVertical = largoPantalla // self.tamañoFotoCelda #20
        self.fondoAgua = self.cargar_foto('imagenes/agua.jpg')
        self.fondoMont = self.cargar_foto('imagenes/piedra3.png')
        self.fondoTier = self.cargar_foto('imagenes/tierra.png')
        self.arbol = self.cargar_foto('imagenes/arbolrefull.png')
        self.hombre = self.cargar_foto('Tropas y personajes/3 Man/Man.png')
        self.manWalk = self.cargar_foto('Tropas y personajes/3 Man/Man_Walk.png')
        self.mapaObj = Mapa()
        self.mapa = self.mapaObj.mapaOculto


    def cargar_foto(self, imagen):
        """Cargo todas las fotos y las escalo al tamaño de las celdas de la matriz"""
        fotoOriginal = pygame.image.load(imagen)
        fotoEscalada = pygame.transform.scale(fotoOriginal, (self.tamañoFotoCelda, self.tamañoFotoCelda))
        return (fotoEscalada)

    def getCeldasPantallaTotales(self):
        """Devuelvo la cantidad de celdas que entran en la pantalla que ve el usuario"""
        return self.celdasPantallaTotalHorizontal, self.celdasPantallaTotalVertical

    def cargar_jugador(self):

        self.screen.blit(self.hombre, (self.mapaObj.playerSpawn()[1] * self.tamañoFotoCelda, self.mapaObj.playerSpawn()[0] * self.tamañoFotoCelda))


    def mostrar_mapa(self):
        """Dibujo el mapa con todos los sprites juntos"""
        forY = 0
        for y in range(self.mapaObj.getCentroPantalla()[1] - (self.celdasPantallaTotalVertical//2), self.mapaObj.getCentroPantalla()[1] + (self.celdasPantallaTotalVertical//2)):
            forX = 0
            for x in range(self.mapaObj.getCentroPantalla()[0] - (self.celdasPantallaTotalHorizontal // 2), self.mapaObj.getCentroPantalla()[0] + (self.celdasPantallaTotalHorizontal // 2)):

                if self.mapa[y][x] == Tierra():

                    self.screen.blit(self.fondoTier, (forX * self.tamañoFotoCelda, forY * self.tamañoFotoCelda)) 
                    if self.mapa[y][x].tiene_arbol():
                        self.screen.blit(self.arbol, (forX * self.tamañoFotoCelda, forY * self.tamañoFotoCelda)) 

                if self.mapa[y][x] == Agua():

                    self.screen.blit(self.fondoAgua, (forX * self.tamañoFotoCelda, forY * self.tamañoFotoCelda)) 

                if self.mapa[y][x] == Montaña():

                    self.screen.blit(self.fondoMont, (forX * self.tamañoFotoCelda, forY * self.tamañoFotoCelda)) 
                    #poner foto piedra

                forX += 1

            forY += 1   
