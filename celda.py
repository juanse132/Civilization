from water import Agua
from tierra import Tierra
from montaña import Montaña


class Celda:
    def __init__(self, is_visible=False):
        self.visible = is_visible
        self.tamañaoCelda = 20
        self.ocupada_con = None

    def get_tamaño(self):
        return self.tamañaoCelda
    
    def ocupada (self):
        pass

    def hayCuidad(self):
        pass
    
    def visibilizar(self):
        self.visible = True