import pygame
from sys import exit
from pygame import time
from random import randint
import numpy as np
from pygame.constants import MOUSEBUTTONDOWN



class Vista:
    def __init__(self, mapa_actual) -> None:
        pygame.init()
        anchoPantalla = 800
        largoPantalla = 400
        self.screen = pygame.display.set_mode((anchoPantalla,largoPantalla))
        pygame.display.set_caption('Civilization')
        self.tamañoFotoCelda = 20 # en pixeles
        self.celdasPantallaTotalHorizontal = anchoPantalla // self.tamañoFotoCelda #40 
        self.celdasPantallaTotalVertical = largoPantalla // self.tamañoFotoCelda #20
        self.anchoMinimo = self.mapa.getCentroPantalla()[1] - (self.celdasPantallaTotalVertical//2)
        self.anchoMaximo = self.mapa.getCentroPantalla()[1] + (self.celdasPantallaTotalVertical//2)
        self.largoMinimo = self.mapa.getCentroPantalla()[0] - (self.celdasPantallaTotalHorizontal // 2)
        self.largoMaximo = self.mapa.getCentroPantalla()[0] + (self.celdasPantallaTotalHorizontal // 2)
        self.fondoAgua = self.cargar_foto('imagenes/agua.jpg')
        self.fondoMont = self.cargar_foto('imagenes/piedra3.png')
        self.fondoTier = self.cargar_foto('imagenes/tierra.png')
        self.arbol = self.cargar_foto('imagenes/arbolrefull.png')
        self.hombre = self.cargar_foto('Tropas y personajes/3 Man/Man.png')
        self.manWalk = self.cargar_foto('Tropas y personajes/3 Man/Man_Walk.png')
        self.mapa = mapa_actual
        self.cargar_sprites()

    def cargar_sprites(self):
        for fila in self.mapa.get_mapa():
            for celda in fila:
                celda.set_sprite(self.cargar_foto(celda.get_url_imagen()))
                recurso = celda.get_recurso()
                if recurso != None:
                    recurso.set_sprite(self.cargar_foto(recurso.get_url_imagen()))
        personaje = self.mapa.get_personaje()
        personaje.set_sprite(self.cargar_foto(personaje.get_url_imagen()))

    def cargar_foto(self, imagen):
        """Cargo todas las fotos y las escalo al tamaño de las celdas de la matriz"""
        fotoOriginal = pygame.image.load(imagen)
        fotoEscalada = pygame.transform.scale(fotoOriginal, (self.tamañoFotoCelda, self.tamañoFotoCelda))
        return (fotoEscalada)
    
    def get_ancho_pantalla(self):
        return self.anchoMinimo, self.anchoMaximo
        
    def get_largo_pantalla(self):    
        return self.largoMinimo, self.largoMaximo

    def getCeldasPantallaTotales(self):
        """Devuelvo la cantidad de celdas que entran en la pantalla que ve el usuario"""
        return self.celdasPantallaTotalHorizontal, self.celdasPantallaTotalVertical

    def mostrar_jugador(self):
        # spawn del jugador
        personaje = self.mapa.get_personaje()
        self.screen.blit(personaje.get_sprite(), (personaje.get_pos()[1] * self.tamañoFotoCelda, personaje.get_pos()[0] * self.tamañoFotoCelda))


    def mostrar_mapa(self):
        """Dibujo el mapa con todos los sprites juntos""" 
        forY = 0
        for y in range(self.anchoMinimo, self.anchoMaximo):
            forX = 0
            for x in range(self.largoMinimo, self.largoMaximo):
                
                self.screen.blit(self.mapa.get_item(y,x).get_sprite(), (forX * self.tamañoFotoCelda, forY * self.tamañoFotoCelda))
                try:
                    self.screen.blit(self.mapa.get_item(y,x).get_recurso().get_sprite(), (forX * self.tamañoFotoCelda, forY * self.tamañoFotoCelda))
                except:
                    pass

            
                forX += 1

            forY += 1   
    
    def moverse_en_pantalla(self):
        movimiento = None


    def get_mouse_pos(self):
        return pygame.mouse.get_pos()

