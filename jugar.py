import pygame
from pantalla import mapacheto
from vista import Vista
from mapa import Mapa

class Juego:
    # Es el controlador
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.mapa = Mapa() # es el modelo
        self.vista = Vista(self.mapa)

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
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1: 
                        pass
                    elif event.button == 3: 
                        pass

            self.vista.mostrar_mapa()
            self.vista.mostrar_jugador()
            

            pygame.display.flip()
            pygame.display.update()
            self.clock.tick(60)
        

    def movimiento_pantalla(self, key):
        """Me muevo por la pantalla hasta los limites de la matriz"""
        if key == pygame.K_UP: 
            self.mapa.set_centro_pantalla_y(-2)
            #self.mapa.set_centro_pantalla_minimo_y(-2)
        if key == pygame.K_DOWN:
            self.mapa.set_centro_pantalla_y(2)
            #self.mapa.set_centro_pantalla_maximo_y(2)
        if key == pygame.K_LEFT:
            self.mapa.set_centro_pantalla_x(-2)
            #self.mapa.set_centro_pantalla_minimo_x(-2)
        if key == pygame.K_RIGHT:
            self.mapa.set_centro_pantalla_x(2)
            #self.mapa.set_centro_pantalla_maximo_x(2)


    def mouse_posicion(self):
        tamañoCelda = 20
        posXMouse, posYMouse = self.vista.get_mouse_pos()
        posXCeldas = (posXMouse//tamañoCelda) # Lo escala al tamaño de las celdas
        posYCeldas = (posYMouse//tamañoCelda)
        #Todo: falta terminar lo de moverse del personaje
        return posXCeldas , posYCeldas

          

juego = Juego()