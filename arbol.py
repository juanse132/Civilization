from celda import Celda
from random import randint

class Arbol(Celda):
    def __init__(self, is_visible=False) -> None:
        super().__init__(is_visible=False)
        self.cantidadMaderaOtorgada = [60, 20, 10, 30]
        self.url_imagen = "imagenes/arbol_nuevo.png"

    def minar(self):
        return self.cantidadMaderaOtorgada[randint(0, 3)], "madera"


