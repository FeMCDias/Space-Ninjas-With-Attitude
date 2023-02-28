import pygame
from interface import *
import screens.gerenciadorTelas as gerenciadorTelas
import os

class Derrota:
    def __init__(self, display):
        font = pygame.font.Font(os.path.join('assets', 'fonts', 'Karasha.ttf'), 50)
        self.next_screen = 'chooseWeapon'
        self.screen_name = 'derrota'
        self.display = display
        self.buttons = []
        self.buttons.append(Button(400, 450, 200, 100, None, (255, 0, 0), font, (0, 0, 0),30))
        self.buttons[0].add_text('Restart')
        self.buttons.append(Button(self.buttons[0].x + self.buttons[0].w + 50, self.buttons[0].y, 200, 100, None, (255, 0, 0), font, (0, 0, 0), 30))
        self.buttons[1].add_text('Quit')
        self.state = {}

    def desenha(self, display):
        fundo = pygame.image.load(os.path.join('assets', 'images', 'back_defeat.jpg'))
        self.display = display
        self.display.blit(fundo, (0, 0))
        for button in self.buttons:
            pygame.draw.rect(self.display, (255, 255, 255), (button.x-5, button.y-5, button.w+10, button.h+10), 5, border_radius=35)
            button.draw(self.display)
        pygame.display.update()

    def atualiza_estado(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.buttons[0].is_clicked(mouse_pos):
                    return gerenciadorTelas.GerenciadorTelas(self.display).set_state(self.next_screen)
                if self.buttons[1].is_clicked(mouse_pos):
                    return False
        return True
    
    def get_state(self):
        return self.state