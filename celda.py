

class Celda:
    def __init__(self, is_visible=True):
        self.visible = is_visible
        self.tamañaoCelda = 20
        self.objetos = []
        self.recurso= None
        self._sprite = None
        self.url_imagen = None

    def set_sprite(self, sprite):
        self._sprite = sprite

    def get_url_imagen(self):
        return self.url_imagen

    def get_sprite(self):
        return self._sprite
    
    def get_tamaño(self):
        return self.tamañaoCelda

    def hayCuidad(self):
        pass
    
    def visibilizar(self):
        self.visible = True
    
    def get_recurso(self):
        return self.recurso


 