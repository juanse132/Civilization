from celda import Celda
import pygame


class Tierra(Celda):
    def __init__(self) -> None:
        self.retrasoMovimientoTierra = 15
        self.celda = Celda()
    
    def cargar_tierra(self):
        fotoOriginal = pygame.image.load('imagenes/tierra.png')
        fotoEscalada = pygame.transform.scale(fotoOriginal, (self.get_tamaño(),self.celda.get_tamaño()))
        return (fotoEscalada)