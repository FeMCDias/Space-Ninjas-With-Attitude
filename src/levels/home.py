import pygame
from interface import *
import levels.level as level

class Home:
    def __init__(self, display):
        self.display = display
        self.buttons = []
        self.buttons.append(Button(100, 100, 200, 100, None, (255, 0, 0), None, (0, 0, 0)))
        self.buttons[0].add_text('Start')
        self.buttons.append(Button(100, 300, 200, 100, None, (255, 0, 0), None, (0, 0, 0)))
        self.buttons[1].add_text('Quit')
        self.state = {}

    def desenha(self, display):
        self.display = display
        for button in self.buttons:
            button.draw(self.display)
        pygame.display.update()

    def atualiza_estado(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.buttons[0].is_clicked(mouse_pos):
                    nivel = level.level()
                    window, assets, state = nivel.inicializa()
                    nivel.gameloop(window, assets, state)
                    nivel.finaliza()
                    return False
                if self.buttons[1].is_clicked(mouse_pos):
                    return False
        return True
    
    def get_state(self):
        return self.state
    
