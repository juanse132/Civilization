import pygame
from sys import exit
from pygame import time
from random import randint

anchoCelda = 20
altoCelda = 20

miArr = ["AGUA", "MONTANA", "TIERRA" , "TIERRA", "TIERRA", "TIERRA", "TIERRA"]

fondoOriginal = None
fondoReload = None

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Civilization')
clock = pygame.time.Clock()



anchoFoto = 0
altoFoto = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if altoFoto != 400 and anchoFoto != 800:


        fondo = miArr[randint(0, 6)]

        #if fondo == miArr[0]:
         #   fondoOriginal = pygame.image.load('imagenes/agua.jpg')
          #  fondoReload = pygame.transform.scale(fondoOriginal, (anchoCelda, altoCelda))

        if fondo == miArr[1]:
            fondoOriginal = pygame.image.load('imagenes/montaña.jpg')
            fondoReload = pygame.transform.scale(fondoOriginal, (anchoCelda, altoCelda))

        elif fondo == miArr[2]:
            fondoOriginal = pygame.image.load('imagenes/tierra.png')
            fondoReload = pygame.transform.scale(fondoOriginal, (anchoCelda, altoCelda))

        screen.blit(fondoReload, (anchoFoto,altoFoto)) 

        anchoFoto += 20
        if anchoFoto == 800:
            anchoFoto = 0
            altoFoto += 20

    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)
