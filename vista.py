import pygame
from sys import exit
from pygame import time
from random import randint
import numpy as np
from pygame.constants import MOUSEBUTTONDOWN



class Vista:
    def __init__(self, mapa_actual, tamanioFotoCelda, anchoLargoPantalla, limites) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((anchoLargoPantalla[0],anchoLargoPantalla[1])) # 800, 400
        pygame.display.set_caption('Civilization')
        self.tamañoFotoCelda = tamanioFotoCelda # en pixeles
        #self.celdasPantallaTotalHorizontal = celdasPantallaTotalHorizontal #40 celdas que entran horizontal en la pantalla
        #self.celdasPantallaTotalVertical = celdasPantallaTotalVertical #20 celdas que entran vertical en la pantalla
        self.recuadro = self.cargar_foto("imagenes/Recuadro_rojo.png")
        self.mapa = mapa_actual
        self.actualizar_pantalla(limites)
        self.cargar_sprites()

    def actualizar_pantalla(self, cosa):
        """Se setea los limites de la pantalla la cual va a ver el usuario"""
        self.yMinimo = cosa[0]
        self.yMaximo = cosa[1]
        self.xMinimo = cosa[2]
        self.xMaximo = cosa[3]


    def cargar_sprites(self):
        """Se cargan todos los sprites"""
        for fila in self.mapa.get_mapa():
            for celda in fila:
                celda.set_sprite(self.cargar_foto(celda.get_url_imagen()))
                recurso = celda.get_recurso()
                if recurso != None:
                    recurso.set_sprite(self.cargar_foto(recurso.get_url_imagen()))
        personaje = self.mapa.get_personaje()
        personaje.set_sprite(self.cargar_foto(personaje.get_url_imagen()))
        guerrero = self.mapa.get_guerrero()
        guerrero.set_sprite(self.cargar_foto(guerrero.get_url_imagen()))


    def cargar_foto(self, imagen):
        """Cargo todas las fotos y las escalo al tamaño de las celdas de la matriz"""
        fotoOriginal = pygame.image.load(imagen)
        fotoEscalada = pygame.transform.scale(fotoOriginal, (self.tamañoFotoCelda , self.tamañoFotoCelda))

        return (fotoEscalada)
    

    def mostrar_jugador(self):
        # spawn del jugador
        personaje = self.mapa.get_personaje()
        self.screen.blit(personaje.get_sprite(), (personaje.get_pos()[1] * self.tamañoFotoCelda, personaje.get_pos()[0] * self.tamañoFotoCelda))
    

    def mostrar_guerrero(self):
        # spawn del guerrero
        guerrero = self.mapa.get_guerrero()
        self.screen.blit(guerrero.get_sprite(), (guerrero.get_pos()[1] * self.tamañoFotoCelda , guerrero.get_pos()[0] * self.tamañoFotoCelda ))
    
    def get_mouse_pos(self):
        return pygame.mouse.get_pos()

    def mostrar_mapa(self):
        """Dibujo el mapa con todos los sprites juntos"""  
        forY = 0
        for y in range(self.yMinimo, self.yMaximo):
            forX = 0
            for x in range(self.xMinimo, self.xMaximo):
                
                self.screen.blit(self.mapa.get_item(y, x).get_sprite(), (forX * self.tamañoFotoCelda, forY * self.tamañoFotoCelda))

                try:
                    self.screen.blit(self.mapa.get_item(y, x).get_recurso().get_sprite(), (forX * self.tamañoFotoCelda, forY * self.tamañoFotoCelda))
                except:
                    pass
                try:
                    self.screen.blit(self.mapa.get_item(y, x).get_personaje().get_sprite(), (forX * self.tamañoFotoCelda, forY  * self.tamañoFotoCelda))
                except:
                   pass
                try:
                    self.screen.blit(self.mapa.get_item(y, x).get_guerrero().get_sprite(), (forX * self.tamañoFotoCelda, forY  * self.tamañoFotoCelda))
                except:
                   pass
                
                forX += 1

            forY += 1 
        self.mostar_recuadro()

        
    def mostar_recuadro(self):
        self.screen.blit(self.recuadro, ((self.get_mouse_pos()[0] // self.tamañoFotoCelda)*self.tamañoFotoCelda, (self.get_mouse_pos()[1]// self.tamañoFotoCelda)*self.tamañoFotoCelda))

