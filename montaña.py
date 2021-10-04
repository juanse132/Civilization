from celda import Celda
import pygame


class Montaña(Celda):
    def __init__(self) -> None:
        super().__init__()
        self.velocidad = 15
        self.celda = Celda()
    
    """def cargar_montaña(self):
        fotoOriginal = pygame.image.load('imagenes/piedra3.png')
        fotoEscalada = pygame.transform.scale(fotoOriginal, (self.celda.get_tamaño(),self.celda.get_tamaño()))
        return (fotoEscalada)"""