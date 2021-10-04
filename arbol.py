from celda import Celda


class Arbol(Celda):
    def __init__(self) -> None:
        super().__init__()
        self.vida = 40
        self.cantidadComidaOtorgada = [60, 20, 10, 30]


    def minado(self):
        pass

