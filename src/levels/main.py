
import pygame
import home

def main():
    pygame.init()
    width = 1200
    height = 700
    display = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    FPS = 60

    level = home.home(display)
    while True:
        if level.atualiza_estado():
            level.desenha()
        else:
            break
        clock.tick(FPS)

if __name__ == '__main__':
    main()
