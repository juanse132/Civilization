from arbol import Arbol
from arbusto import Arbusto
from piedra import Piedra
from vaca import Vaca
from water import Agua
from tierra import Tierra
from montaña import Montaña


class Celda:
    def __init__(self, tipo, is_visible=False):
        self.visible = is_visible
        self.tamañaoCelda = 20
        self.objetos = [Piedra, Arbol, Arbusto, Vaca]
        self.recurso= ["Arbol"]
        self.tipo = tipo()

    def get_tamaño(self):
        return self.tamañaoCelda


    def get_tipo(self):
        return self.tipo 

    def obtenerPiedra(self):
        return self.tipo.get_piedra()

    def obtenerArbol(self):
        return self.tipo.get_arbol()

    def hayCuidad(self):
        pass
    
    def visibilizar(self):
        self.visible = True


 