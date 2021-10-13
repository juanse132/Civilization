from celda import Celda

class Arbol(Celda):
    def __init__(self) -> None:
        super().__init__(Arbol, is_visible=False)
        self.vida = 40
        self.cantidadMaderaOtorgada = [60, 20, 10, 30]


    def minado(self):
        pass

    def tiene_piedra(self):
        return False