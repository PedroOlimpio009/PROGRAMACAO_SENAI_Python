import pygame
import sys
import random
from quadrado import Quadrado

class Jogo:
    def __init__(self):
        pygame.init()
        self.largura = 800
        self.altura = 600
        self.tela = pygame.display.set_mode((self.largura, self.altura))
        pygame.display.set_caption("Caça-Quadrado")
        self.fonte = pygame.font.Font(None, 36)
        self.relogio = pygame.time.Clock()
        self.tempo_limite = 30_000  # 30 segundos
        self.inicio = None
        self.pontuacao = 0
        self.rodando = False
        self.quadrado = Quadrado(self.largura, self.altura, (255, 0, 0))
        self.recorde = self.carregar_recorde()

    def carregar_recorde(self):
        try:
            with open("recorde.txt", "r") as arquivo:
                return int(arquivo.read())
        except FileNotFoundError:
            return 0

    def salvar_recorde(self):
        with open("recorde.txt", "w") as arquivo:
            arquivo.write(str(self.recorde))

    def mostrar_texto(self, texto, x, y):
        texto_renderizado = self.fonte.render(texto, True, (0, 0, 0))
        self.tela.blit(texto_renderizado, (x, y))


    def executar(self):
        self.inicio = pygame.time.get_ticks()
        self.rodando = True

        while self.rodando:
            self.tela.fill((202, 187, 179))
            tempo_atual = pygame.time.get_ticks()
            tempo_restante = self.tempo_limite - (tempo_atual - self.inicio)
            if tempo_restante <= 0:
                self.rodando = False
                tempo_restante = 0

            self.mostrar_texto(f"Tempo restante: {tempo_restante // 1000} s", 10, 10)
            self.mostrar_texto(f"Pontos: {self.pontuacao}", 10, 50)
            self.mostrar_texto(f"Recorde: {self.recorde}", 10, 90)
            self.quadrado.desenhar(self.tela)
            pygame.display.flip()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.rodando = False
                elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    if self.quadrado.foi_clicado(evento.pos):
                        self.pontuacao += 1
                        self.quadrado.mover()
                        self.quadrado.cor = (
                            pygame.Color(
                                random.randint(0, 255),
                                random.randint(0, 255),
                                random.randint(0, 255),
                            )
                        )
                        if self.pontuacao % 5 == 0:
                            self.quadrado.tamanho = max(20, self.quadrado.tamanho - 5)

            self.relogio.tick(60)

        if self.pontuacao > self.recorde:
            self.recorde = self.pontuacao
            self.salvar_recorde()

        self.mostrar_texto("Fim de Jogo!", self.largura // 2 - 100, self.altura // 2)
        pygame.display.flip()
        pygame.time.wait(3000)
        pygame.quit()
        sys.exit()

