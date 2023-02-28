
import pygame
import screens.gerenciadorTelas
import os

def main(): 
    pygame.init()
    width = 1220
    height = 650
    icon = pygame.image.load(os.path.join('src','assets', 'images', 'icon.png'))
    pygame.display.set_icon(icon)
    pygame.display.set_caption('Space Ninjas With Attitude')
    display = pygame.display.set_mode((width, height))
    screen = screens.gerenciadorTelas.GerenciadorTelas(display)
    screen.game_loop()
    screen.finaliza()

if __name__ == '__main__':
    main()