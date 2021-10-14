from celda import Celda


class Arbusto(Celda):
    def __init__(self) -> None:
        super().__init__()
        self.vida = 30
        self.cantidadComidaOtorgada = [60, 20, 50, 70, 35]
        self.url_imagen_recurso = "imagenes/arbusto_nuevo.png"

    def minado(self):
        pass

