import pygame
from pantalla import mapacheto
from vista import Vista

class Juego:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.vista = Vista()

        self.jugar()


    def jugar(self):
        while True:
            for event in pygame.event.get():
                rightClicking = False
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    #self.mapa.movimiento_pantalla(event.key)
                    pass
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1: 
                        pass
                    elif event.button == 3: 
                        pass

            self.vista.mostrar_mapa()
            

            pygame.display.flip()
            pygame.display.update()
            self.clock.tick(60)

juego = Juego()