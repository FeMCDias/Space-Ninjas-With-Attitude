import pygame
import numpy as np

pygame.init()
pygame.mouse.set_visible(True)
# Tamanho da tela e definição do FPS
BLACK = (0, 0, 0)
screen = pygame.display.set_mode((1244, 700))
clock = pygame.time.Clock()
FPS = 60  # Frames per Second


rodando = True
while rodando:
    # Capturar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
    if event.type == pygame.KEYDOWN:
        pass

    # Controlar frame rate
    clock.tick(FPS)


    # Desenhar fundo
    screen.fill(BLACK)

    # Update!
    pygame.display.update()

# Terminar tela
pygame.quit()