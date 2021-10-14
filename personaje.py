from mapa import Mapa
import pygame
from celda import Celda 
from vista import Vista

class Personaje:
    def __init__(self):
        self.estado = True
        self.vida = None
        self.velocidad = None
        self.celdas_visibles = 4
        self.comida = None
        self.url_imagen = "Tropas y personajes/3 Man/Man.png"
        self._sprite = None
    
    def set_sprite(self, sprite):
        self._sprite = sprite

    def get_pos(self):
        pass
 
    def moverse(self):
        """Genero el moviemiento del personaje haciendo clicks"""
        #self.mapa.mapaObjetos[self.posicionPersonajeY][self.posicionPersonajeX] = 0
        mousePosX, mousePosY = pygame.mouse.get_pos()
        posXCeldas = (mousePosX//self.celda.get_tamaño()) # Lo escala al tamaño de las celdas
        posYCeldas = (mousePosY//self.celda.get_tamaño()) 
        centroPantallaX, centroPantallaY = self.mapa.getCentroPantalla()
        self.posicionPersonajeX = posXCeldas + centroPantallaX - (self.vista.getCeldasPantallaTotales()[0]) 
        self.posicionPersonajeY = posYCeldas + centroPantallaY - (self.vista.getCeldasPantallaTotales()[1]) 
        self.mapa.descubirMapa(self.posicionPersonajeY,self.posicionPersonajeX, self.celdas_visibles)