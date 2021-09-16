import pygame
from pantalla import mapacheto

class Juego:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.mapa = mapacheto()

        self.jugar()
 
    def jugar(self):
        while True:
            for event in pygame.event.get():
                rightClicking = False
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    self.mapa.movimiento_pantalla(event.key)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1: 
                        self.mapa.mover_personaje()
                    elif event.button == 3: 
                        rightClicking = True

            self.mapa.mostrar_mapa()

            pygame.display.flip()
            pygame.display.update()
            self.clock.tick(60)

juego = Juego()