from water import Agua
from tierra import Tierra
from montaña import Montaña


class Celda:
    def __init__(self):
        self.visible = None
        self.tamañaoCelda = 20
        self.pisable = None
        self.agua = Agua()
        self.montaña = Montaña()
        self.tierra = Tierra()


    def get_tamaño(self):
        return self.tamañaoCelda
    
    def pisar(self):
        if self.agua.tiempo() == 0:
            self.pisable = False
        elif self.montaña.tiempo() == 3:
            self.pisable = True
        elif self.tierra.tiempo() == 1:
            self.pisable = True
        return self.pisable

    def ocuapda (self):
        pass

    def hayCuidad(self):
        pass