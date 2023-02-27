
import pygame
import screens.gerenciadorTelas

def main():
    pygame.init()
    width = 1220
    height = 650
    display = pygame.display.set_mode((width, height))
    screen = screens.gerenciadorTelas.GerenciadorTelas(display)
    screen.game_loop()
    screen.finaliza()


if __name__ == '__main__':
    main()