from celda import Celda
from random import randint


class Piedra(Celda):
    def __init__(self, is_visible=False) -> None:
        super().__init__(is_visible=False)
        self.cantidadHierroPiedraOtorgada = [10, 20, 5, 15, 30, 40, 25, 6, 35, 60]
        self.tipos = ["hierro", "piedra"]
        self.url_imagen = "imagenes/piedra3.png"


    def minar(self):
        return self.cantidadHierroPiedraOtorgada[randint(0, 9)], self.tipos[randint(0, 1)]


    def isSpawnable(self):
        return False

    
