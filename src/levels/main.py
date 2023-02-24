# rodar o jogo, apenas com o level.py

import pygame
import pymunk as pm
import home

def main():
    pygame.init()
    width = 1200
    height = 700
    display = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    home.home(display, clock)
    

    # nivel = level.level()
    # window, assets, state = nivel.inicializa()
    # nivel.gameloop(window, assets, state)
    # nivel.finaliza()

if __name__ == '__main__':
    main()
