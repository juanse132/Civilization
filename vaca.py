from celda import Celda


class Vaca(Celda):
    def __init__(self) -> None:
        super().__init__()
        self.vida = 25
        self.tiempoParaMatar = 10
        self.cantidadComidaOtorgada = [60, 50, 70]


    def muerta(self):
        pass

    def domesticada(self):
        pass

