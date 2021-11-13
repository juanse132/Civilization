import pygame
from vista import Vista
from mapa import Mapa

class Juego:
    # Es el controlador
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.tamanioFotoCelda = 20
        self.anchoLargoPantalla = [800, 400]
        self.celdasPantallaTotalHorizontal = self.anchoLargoPantalla[0] // self.tamanioFotoCelda #40 
        self.celdasPantallaTotalVertical = self.anchoLargoPantalla[1] // self.tamanioFotoCelda #20
        self.mapa = Mapa() # es el modelo
        self.vista = Vista(self.mapa, self.tamanioFotoCelda, self.anchoLargoPantalla, self.setear_pantalla())

        self.jugar()


    def jugar(self): 
        while True:   
            for event in pygame.event.get():
                rightClicking = False
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    self.movimiento_pantalla(event.key)
                    self.vista.actualizar_pantalla(self.setear_pantalla())
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.mapa.get_item(self.mouse_posicion()[1], self.mouse_posicion()[0]).isSpawnable() == True:
                            self.mapa.get_personaje().mover_personaje(self.mouse_posicion(), self.mapa)
                    elif event.button == 3: 
                        if self.mapa.get_item(self.mouse_posicion()[1], self.mouse_posicion()[0]).isSpawnable() == True:
                            self.mapa.get_guerrero().mover_guerrero(self.mouse_posicion(), self.mapa)

            self.vista.mostrar_mapa()
            self.vista.mostrar_jugador()
            self.vista.mostrar_guerrero()
            
            pygame.display.flip()
            pygame.display.update()
            self.clock.tick(60)
        

    def movimiento_pantalla(self, key):
        """Me muevo por la pantalla hasta los limites de la matriz"""
        if key == pygame.K_UP: 
            self.mapa.set_centro_pantalla_y(-2)
        if key == pygame.K_DOWN:
            self.mapa.set_centro_pantalla_y(2)
        if key == pygame.K_LEFT:
            self.mapa.set_centro_pantalla_x(-2)
        if key == pygame.K_RIGHT:
            self.mapa.set_centro_pantalla_x(2)


    def mouse_posicion(self):
        """Saco la posicion del mouse y la transformo a celda para luego mover al personaje"""
        posXMouse, posYMouse = self.vista.get_mouse_pos()
        posXCeldas = (posXMouse//self.tamanioFotoCelda) + self.xMinimo# Lo escala al tamaño de las celdas
        posYCeldas = (posYMouse//self.tamanioFotoCelda) + self.yMinimo
        #Todo: falta terminar lo de moverse del personaje
        return (posXCeldas , posYCeldas)


    def setear_pantalla(self):
            """Se setea los limites de la pantalla la cual va a ver el usuario"""
            self.yMinimo = self.mapa.getCentroMapa()[1] - (self.celdasPantallaTotalVertical//2) #40
            self.yMaximo = self.mapa.getCentroMapa()[1] + (self.celdasPantallaTotalVertical//2) #60
            self.xMinimo = self.mapa.getCentroMapa()[0] - (self.celdasPantallaTotalHorizontal // 2) #30
            self.xMaximo = self.mapa.getCentroMapa()[0] + (self.celdasPantallaTotalHorizontal // 2) #70
            return self.yMinimo, self.yMaximo, self.xMinimo, self.xMaximo

          

juego = Juego()