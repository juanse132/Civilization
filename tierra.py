from celda import Celda
import pygame
from arbol import Arbol
from numpy import random
from random import randint


class Tierra(Celda):
    def __init__(self) -> None:
        super().__init__()
        self.velocidad = 1
        self.celda = Celda()
        self.arbol = None
    
    """def cargar_tierra(self):
        fotoOriginal = pygame.image.load('imagenes/tierra.png')
        fotoEscalada = pygame.transform.scale(fotoOriginal, (self.get_tamaño(),self.celda.get_tamaño()))
        return (fotoEscalada)"""
    
    def tiempo(self):
        return self.velocidad

    def tiene_arbol(self):
        num = randint(9,100)
        
        if num > 75:
            self.arbol = Arbol()
            return True
        else:
            return False
    
    def get_arbol(self):
        return self.arbol