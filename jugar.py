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
                    self.vista.movimiento_pantalla(event.type)
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

          

juego = Juego()