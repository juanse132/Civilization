import pygame

class Personaje:
    def __init__(self, posicion):
        self.estado = True
        self.vida = None
        self.velocidad = None
        self.celdas_visibles = 4
        self.url_imagen = "Tropas y personajes/GraveRobber.png"
        self._sprite = None
        self.posX = posicion[1]
        self.posY = posicion[0]
        self.inventario = {"madera": 0, "piedra": 0, "hierro": 0, "comida": 0}
    
    def set_sprite(self, sprite):
        """Seteo el sprite"""
        self._sprite = sprite

    def get_url_imagen(self):
        """Obtengo la url de la imagen que voy a cargar y la devuelo"""
        return self.url_imagen

    def get_sprite(self):
        """devuelvo el sprite"""
        return self._sprite

    def get_pos(self):
        return self.posY, self.posX
    
    def mover_personaje(self, posicionNueva, mapa):
        """Cargo la nueva posicion del personaje para luego moverme por el mapa"""
        mapa.get_celda(self.posY, self.posX).un_set_personaje()
        self.posY = posicionNueva[1] 
        self.posX = posicionNueva[0] 
        mapa.get_celda(self.posY, self.posX).set_personaje(self)


    def agregar_recurso(self, tipo, cantidad):
        """Agrego al inventario del personaje la cantidad de recurso que consiguio minando"""
        self.inventario[tipo] += cantidad

    def get_inventario(self):
        return self.inventario

    def isMiniable(self):
        return True

    def minar_vaca(self):
        return False