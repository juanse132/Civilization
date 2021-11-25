from celda import Celda
from random import randint

class Arbusto(Celda):
    def __init__(self, is_visible=False) -> None:
        super().__init__(is_visible=False)
        self.cantidadComidaOtorgada = [60, 20, 50, 70, 35]
        self.url_imagen= "imagenes/arbusto_nuevo.png"

    def minar(self):
        return self.cantidadComidaOtorgada[randint(0, 4)], "comida"




