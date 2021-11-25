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
                personaje = celda.get_personaje()
                if personaje != None:
                    personaje.set_sprite(self.cargar_foto(personaje.get_url_imagen()))
    

    def cargar_foto(self, imagen):
        """Cargo todas las fotos y las escalo al tamaño de las celdas de la matriz"""
        fotoOriginal = pygame.image.load(imagen)
        fotoEscalada = pygame.transform.scale(fotoOriginal, (self.tamañoFotoCelda , self.tamañoFotoCelda))

        return (fotoEscalada)
    

    def get_mouse_pos(self):
        return pygame.mouse.get_pos()


    def mostrar_mapa(self):
        """Dibujo el mapa con todos los sprites juntos en la pantalla que ve el usuario"""  
        forY = 0
        for y in range(self.yMinimo, self.yMaximo):
            forX = 0
            for x in range(self.xMinimo, self.xMaximo):
                
                self.screen.blit(self.mapa.get_celda(y, x).get_sprite(), (forX * self.tamañoFotoCelda, forY * self.tamañoFotoCelda))

                try:
                    self.screen.blit(self.mapa.get_celda(y, x).get_recurso().get_sprite(), (forX * self.tamañoFotoCelda, forY * self.tamañoFotoCelda))
                except:
                    pass
                try:
                    self.screen.blit(self.mapa.get_celda(y, x).get_personaje().get_sprite(), (forX * self.tamañoFotoCelda, forY  * self.tamañoFotoCelda))
                except:
                   pass
                
                forX += 1

            forY += 1 
        self.mostar_recuadro()

        
    def mostar_recuadro(self):
        self.screen.blit(self.recuadro, ((self.get_mouse_pos()[0] // self.tamañoFotoCelda)*self.tamañoFotoCelda, (self.get_mouse_pos()[1]// self.tamañoFotoCelda)*self.tamañoFotoCelda))


    def mostar_inventario_personajes(self, personaje):
        BLANCO = (255, 255, 255)
        pos =  400
        fuente = pygame.font.SysFont(None, 30)
        for resources, resources_value in personaje.get_inventario().items():
            txt = resources + ": " + str(resources_value)
            texto = fuente.render(txt, True, BLANCO)
            self.screen.blit(texto, (pos, 10))
            pos += 100

                   