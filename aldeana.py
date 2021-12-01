from personaje import Personaje

class Aldeana(Personaje):
    def __init__(self, posicion):
        super().__init__(posicion)
        self.url_imagen = "Tropas y personajes/Woman.png"
    

