import pygame

class Personaje:
    def __init__(self, posicion):
        self.estado = True
        self.vida = None
        self.velocidad = None
        self.celdas_visibles = 4
        self.comida = None
        self.url_imagen = "Tropas y personajes/3 Man/Man.png"
        self._sprite = None
        self.posX = posicion[1]
        self.posY = posicion[0]
    
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
 
    def moverse(self, posicion):
        """Genero el moviemiento del personaje haciendo clicks"""
        #self.mapa.mapaObjetos[self.posicionPersonajeY][self.posicionPersonajeX] = 0 
        #centroPantallaX, centroPantallaY = self.mapa.getCentroPantalla()
        #self.posicionPersonajeX = posXCeldas + centroPantallaX - (self.vista.getCeldasPantallaTotales()[0]) 
        #self.posicionPersonajeY = posYCeldas + centroPantallaY - (self.vista.getCeldasPantallaTotales()[1]) 
       # self.mapa.descubirMapa(self.posicionPersonajeY,self.posicionPersonajeX, self.celdas_visibles)