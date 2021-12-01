from personaje import Personaje


class Aldeano(Personaje):
    def __init__(self, posicion):
        super().__init__(posicion)
        self.url_imagen = "Tropas y personajes/GraveRobber.png"
          
    def minar(self, celda, recurso):
        try:
            if recurso.matable_por() == "aldeana":
                pass
        except:
            cantidad, tipo = recurso.minar()
            self.agregar_recurso(tipo, cantidad)
            celda.un_set_recurso()