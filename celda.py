

class Celda:
    def __init__(self, is_visible=True):
        self.visible = is_visible
        self.tamañaoCelda = 20
        self.objetos = []
        self.recurso= ["Arbol"]

    def get_tamaño(self):
        return self.tamañaoCelda

    def hayCuidad(self):
        pass
    
    def visibilizar(self):
        self.visible = True


 