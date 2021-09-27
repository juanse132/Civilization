import pygame


class Celda:
    def __init__(self):
        self.retrasoMovimiento = 10
        self.tamañaoCelda = 20


    def get_tamaño(self):
        return self.tamañaoCelda