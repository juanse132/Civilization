from celda import Celda
import pygame
from numpy import random
from random import randint


class Tierra(Celda):
    def __init__(self, is_visible=False) -> None:
        super().__init__(is_visible=False)
        self.recurso = None
        self.velocidad = 1
        self.url_imagen = "imagenes/tierra.png"
        self.set_arbol()
        
    """def cargar_tierra(self):
        fotoOriginal = pygame.image.load('imagenes/tierra.png')
        fotoEscalada = pygame.transform.scale(fotoOriginal, (self.get_tamaño(),self.celda.get_tamaño()))
        return (fotoEscalada)"""
    
    def tiempo(self):
        return self.velocidad

    def set_arbol(self):
        from arbol import Arbol
        num = randint(9,100)
        if num > 90:
            self.recurso = Arbol()
            return True
        else:
            return False
    
    def get_recurso(self):
        return self.recurso



    def isSpawnable(self):
        return True