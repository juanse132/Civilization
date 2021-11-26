from celda import Celda
from tierra import Tierra
from random import randint


class Vaca(Celda):
    def __init__(self, is_visible=False) -> None:
        super().__init__(is_visible=False)
        self.cantidadComidaOtorgada = [10, 20, 30]
        self.url_imagen= "imagenes/vaca.png"

    def minar(self):
        return self.cantidadComidaOtorgada[randint(0, 2)], "comida"

    def isMiniable(self):
        return False

