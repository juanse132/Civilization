from celda import Celda
from piedra import Piedra
import pygame
from numpy import random
from random import randint


class Montaña(Celda):
    def __init__(self,is_visible=False) -> None:
        super().__init__(is_visible=False)
        self.velocidad = 3
        self.piedra = None
    
    """def cargar_montaña(self):
        fotoOriginal = pygame.image.load('imagenes/piedra3.png')
        fotoEscalada = pygame.transform.scale(fotoOriginal, (self.celda.get_tamaño(),self.celda.get_tamaño()))
        return (fotoEscalada)"""

    def isSpawnable(self):
        return False

    def tiempo(self):
        return self.velocidad

    def tiene_piedra(self):
        num = randint(9,100)
        if num > 85:
            self.piedra = Piedra()
            return True
        else:
            return False

    def get_piedra(self):
        return self.piedra