from celda import Celda





class Piedra(Celda):
    def __init__(self) -> None:
        super().__init__()
        self.vida = 60
        self.cantidadHierroOtorgado = [10, 20, 5, 15, 30]
        self.cantidadPiedraOtorgada = [40, 25, 6, 35, 60]


    def minado(self):
        pass

