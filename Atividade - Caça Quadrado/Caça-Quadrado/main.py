import pygame 
import pygame_gui
from jogo import Jogo

pygame.init()

# Tamanho da janela
largura = 800
altura = 600

janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Menu Inicial")

# Carrega imagem de fundo
fundo = pygame.image.load("fundo.jpg")
fundo = pygame.transform.scale(fundo, (largura, altura))  # Ajusta ao tamanho da tela


# Gerenciador de UI
gerenciador_ui = pygame_gui.UIManager((largura, altura))

# Botão Start
botao_start = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((largura//2 - 75, altura//2 - 25), (150, 50)),
    text='Start',
    manager=gerenciador_ui
)

rodando = True

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.USEREVENT:
            if evento.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if evento.ui_element == botao_start:
                    jogo = Jogo()
                    jogo.executar() 

        gerenciador_ui.process_events(evento)

    gerenciador_ui.update(0.016)  
    janela.blit(fundo, (0, 0))
    gerenciador_ui.draw_ui(janela)
    pygame.display.update()

pygame.quit()

