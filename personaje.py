from mapa import Mapa
import pygame
from celda import Celda 

class Personaje:
    def __init__(self):
        self.estado = True
        self.vida = None
        self.velocidad = None
        self.celdas_visibles = None
        self.comida = None
        self.mapa = Mapa()
        self.celda = Celda()

    def get_pos(self):
        pass
 
    def moverse(self):
        """Genero el moviemiento del personaje haciendo clicks"""
        self.mapa.mapaObjetos[self.posicionPersonajeY][self.posicionPersonajeX] = 0
        mousePosX, mousePosY = pygame.mouse.get_pos()
        posXCeldas = (mousePosX//self.celda.get_tamaño()) # Lo escala al tamaño de las celdas
        posYCeldas = (mousePosY//self.celda.get_tamaño()) 
        self.posicionPersonajeX = posXCeldas + self.centroPantallaX - (self.celdasPantallaTotalHorizontal//2) 
        self.posicionPersonajeY = posYCeldas + self.centroPantallaY - (self.celdasPantallaTotalVertical//2) 
        self.mapa.mapaObjetos[self.posicionPersonajeY][self.posicionPersonajeX] = -1