# rodar o jogo, apenas com o level.py

import pygame
import pymunk as pm
import level

def main():
    nivel = level.level()
    window, assets, state = nivel.inicializa()
    nivel.gameloop(window, assets, state)
    nivel.finaliza()

if __name__ == '__main__':
    main()
