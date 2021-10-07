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
    
    def ocupada (self):
        tipos = None
        objeto = None
        if self.tipo == Tierra():
            tipos = self.tipo

            if self.tipo.tiene_arbol() == Arbol():
                objeto = self.tipo.tiene_arbol()

        elif self.tipo == Agua():
            tipos = self.tipo

        elif self.tipo == Montaña():
            tipos = self.tipo

            if self.tipo.tiene_piedra() == Piedra():
                objeto = self.tipo.tiene_piedra()
        
        return tipos,objeto

    def get_tipo(self):
        return self.tipo 

    def get_objeto(self):
        return self.tipo.get_piedra()


    def hayCuidad(self):
        pass
    
    def visibilizar(self):
        self.visible = True


 