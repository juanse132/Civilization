from celda import Celda
from random import randint


class Montaña(Celda):
    def __init__(self,is_visible=False) -> None:
        super().__init__(is_visible=False)
        self.velocidad = 3
        self.recurso = None
        self.url_imagen = "imagenes/montaña.jpg"
        self.set_piedra()
    
    """def cargar_montaña(self):
        fotoOriginal = pygame.image.load('imagenes/piedra3.png')
        fotoEscalada = pygame.transform.scale(fotoOriginal, (self.celda.get_tamaño(),self.celda.get_tamaño()))
        return (fotoEscalada)"""

    def isSpawnable(self):
        return False

    def tiempo(self):
        return self.velocidad

    def set_piedra(self):
        from piedra import Piedra
        num = randint(9,100)
        if num > 85:
            self.recurso = Piedra()
            return True
        else:
            return False

    def get_recurso(self):
        return self.recurso

    
    def isSpawnableRecurso(self):
        if self.recurso != None:
            return True
        else:
            return False