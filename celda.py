

class Celda:
    def __init__(self, is_visible=False):
        # TODO: areglar lo de que no se vea el mapa
        self.visible = is_visible
        self.tamañaoCelda = 20
        self.recurso= None
        self._sprite = None
        self.url_imagen = None
        self.personaje = None

    def set_sprite(self, sprite):
        self._sprite = sprite

    def get_url_imagen(self):
        return self.url_imagen

    def get_sprite(self):
        return self._sprite
    
    def get_tamaño(self):
        return self.tamañaoCelda

    def visibilizar(self):
        self.visible = True
    
    def get_recurso(self):
        return self.recurso
    
    def un_set_recurso(self):
        self.recurso = None
    
    def set_personaje(self, personaje):
        self.personaje = personaje

    def get_personaje(self):
        return self.personaje

    def un_set_personaje(self):
        self.personaje = None

    def isSpawnable(self):
        """Verifico si hay un recurso o un personaje en la celda para posteriormente mover al personaje por el mapa"""
        if not self.recurso and not self.personaje:
            return True
        else:
            return False
        
    def minar_recurso(self, personaje):
        """
        Mino el recurso que tiene la celda, guardando el tipo y la cantidad que se consiguio
        luego me traigo que personaje mino ese recurso, para posteriormente agregar la cantidad del recurso minado a su inventario
        y ya luego quito el recurso del mapa
        """
        if personaje.isMiniable() == True:
            cantidad, tipo = self.recurso.minar()
            personaje.agregar_recurso(tipo, cantidad)
            self.un_set_recurso()


    
