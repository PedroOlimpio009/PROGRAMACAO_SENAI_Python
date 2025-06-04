import pygame
import random

class Quadrado:
    def __init__(self, largura, altura, cor):
        self.tamanho = 60
        self.largura_tela = largura
        self.altura_tela = altura
        self.cor = cor
        self.mover()

    def mover(self):
        self.x = random.randint(0, self.largura_tela - self.tamanho)
        self.y = random.randint(0, self.altura_tela - self.tamanho)

    def desenhar(self, tela):
        pygame.draw.rect(tela, self.cor, (self.x, self.y, self.tamanho, self.tamanho))

    def foi_clicado(self, pos_mouse):
        return (self.x <= pos_mouse[0] <= self.x + self.tamanho and
                self.y <= pos_mouse[1] <= self.y + self.tamanho)