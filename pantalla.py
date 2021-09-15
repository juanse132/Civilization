import pygame
from sys import exit
from pygame import time
from random import randint
import numpy as np
from pygame.constants import MOUSEBUTTONDOWN


anchoCelda = 20
altoCelda = 20


anchoPantalla = 800
largoPantalla = 400
fondoOriginal = None
fondoReload = None
fondo = None
fondoADibujar = None
fondoObjetos = None

pygame.init()
screen = pygame.display.set_mode((anchoPantalla,largoPantalla))
pygame.display.set_caption('Civilization')
clock = pygame.time.Clock()

celdasHorizontal = anchoPantalla // anchoCelda #40 
celdasVertical = largoPantalla // altoCelda #20

anchoFoto = 20
altoFoto = 20

columna = 60
fila = 60
maxNegativa = 0
maxPositiva = 30


clicking = False
rightClicking = False

def crear_mapa(fila, columna, valor):
    """Se crea la matriz para el mapa del juego"""
    tablero = []
    for i in range (fila):
        tablero.append([])
        for j in range (columna):
            tablero[i].append(valor)
    return tablero

def mostar_mapa(tablero):
    """Muestro el mapa"""
    for fila in tablero:
        for elem in fila:
            print(elem, end=" ")
        print()


def construir_mapa(mapa):
    x = 0 
    y = 0
    muros = []
    for fila in mapa:
        for muro in fila:
            if muro == "X":
                muros.append(pygame.Rect(x, y, 20, 20))
            x += 20
        x = 0
        y += 20
    return muros

"""def dibujar_mapa(superficie, muros):
    for muro in muros:
        dibujar_agua(superficie, muro)"""

"""def dibujar_agua(superficie, foto):
    aguaOriginal = pygame.image.load('imagenes/agua.jpg')
    foto = pygame.transform.scale(testGroundOriginal, (anchoCelda, altoCelda))
    screen.blit(foto, (0, 0))
    pygame.display.flip()"""

fondoAgua = pygame.image.load('imagenes/agua.jpg')
fondoAguaScaled = pygame.transform.scale(fondoAgua, (anchoCelda, altoCelda))
fondoMont = pygame.image.load('imagenes/montaña.jpg')
fondoMontScaled = pygame.transform.scale(fondoMont, (anchoCelda, altoCelda))
fondoTier = pygame.image.load('imagenes/tierra.png')
fondoTierScaled = pygame.transform.scale(fondoTier, (anchoCelda, altoCelda))
arbol = pygame.image.load('imagenes/arbolrefull.png')
arbolScaled = pygame.transform.scale(arbol, (anchoCelda, altoCelda))
hombre = pygame.image.load('Tropas y personajes/3 Man/Man.png')
hombreScaled = pygame.transform.scale(hombre, (anchoCelda, altoCelda))
manWalk = pygame.image.load('Tropas y personajes/3 Man/Man_Walk.png')
manWalkScaled = pygame.transform.scale(manWalk, (anchoCelda, altoCelda))

mapa =  np.random.randint(0, 100,(fila,columna))
mapaObjetos = np.random.randn(fila, columna)

posX = 60 // 2
posY = 60 // 2

while True:
    for event in pygame.event.get():
        rightClicking = False
        mx, my = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                posY -= 2
                if posY <= maxNegativa:
                    posY = maxNegativa
            if event.key == pygame.K_DOWN:
                posY += 2
                if posY >= maxPositiva:
                    posY = maxPositiva
            if event.key == pygame.K_LEFT:
                posX -= 2
                if posX <= maxNegativa:
                    posX = maxNegativa
            if event.key == pygame.K_RIGHT:
                posX += 2
                if posX >= maxPositiva:
                    posX = maxPositiva
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: 
                clicking = True
                if clicking:
                    posXMouse = mx
                    posYMouse = my
            elif event.button == 3: 
                rightClicking = True
                if rightClicking:
                    posXMouse = mx
                    posYMouse = my
                    if posXMouse == mx and posYMouse == my:
                        screen.blit(hombreScaled, (posXMouse, posYMouse))
    forY = 0

    for y in range(posY - (celdasVertical // 2), posY + (celdasVertical // 2)):

        forX = 0

        for x in range(posX - (celdasHorizontal // 2), posX + (celdasHorizontal // 2)):

            fondo = mapa[y][x]
            fondoObjetos = mapaObjetos[y][x]
            

            if 0 <= fondo <= 1:
                fondoADibujar = fondoAguaScaled
            elif 2 <= fondo <= 4:
                fondoADibujar = fondoMontScaled
            elif 5 <= fondo <= 100:
                fondoADibujar = fondoTierScaled

            screen.blit(fondoADibujar, (forX * anchoFoto, forY * altoFoto)) 

            if 5 <= fondo <= 15:
                screen.blit(arbolScaled, (forX * anchoFoto, forY * altoFoto)) 

            if fondoObjetos == mapaObjetos[30][30]:
                screen.blit(hombreScaled, (forX * anchoFoto, forY * altoFoto))

            forX += 1

        forY += 1
  
    
    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)
