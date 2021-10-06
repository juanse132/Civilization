import pygame
from sys import exit
from pygame import time
from random import randint
import numpy as np
from pygame.constants import MOUSEBUTTONDOWN


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


    def cargar_foto(self, imagen):
        """Cargo todas las fotos y las escalo al tamaño de las celdas de la matriz"""
        fotoOriginal = pygame.image.load(imagen)
        fotoEscalada = pygame.transform.scale(fotoOriginal, (self.tamañoFotoCelda, self.tamañoFotoCelda))
        return (fotoEscalada)

    def getCeldasPantallaTotales(self):
        return self.celdasPantallaTotalHorizontal, self.celdasPantallaTotalVertical
