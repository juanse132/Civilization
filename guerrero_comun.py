from personaje import Personaje

class Guerrero_comun(Personaje):
    def __init__(self, posicion):
        super().__init__(posicion)
        self.url_imagen = "Tropas y personajes/SteamMan.png"
    
    
    def defender(self):
        pass

    def atacar(self):
        pass