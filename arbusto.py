from celda import Celda


class Arbusto(Celda):
    def __init__(self) -> None:
        super().__init__()
        self.vida = 30
        self.cantidadComidaOtorgada = [60, 20, 50, 70, 35]


    def minado(self):
        pass

