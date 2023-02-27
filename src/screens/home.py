import pygame
from interface import *
import fases.level as level
import screens.chooseWeapon as chooseWeapon
import os

class Home:
    def __init__(self, display):
        font = pygame.font.Font(os.path.join('src','assets', 'fonts', 'Karasha.ttf'), 50)
        self.display = display
        self.buttons = []
        self.buttons.append(Button(400, 450, 200, 100, None, (255, 0, 0), font, (0, 0, 0),30))
        self.buttons[0].add_text('Start')
        self.buttons.append(Button(self.buttons[0].x + self.buttons[0].w + 50, self.buttons[0].y, 200, 100, None, (255, 0, 0), font, (0, 0, 0), 30))
        self.buttons[1].add_text('Quit')
        self.state = {}

    def desenha(self, display):
        fundo = pygame.image.load(os.path.join('src','assets', 'images', 'space-ninja-temple.jpg'))
        font = pygame.font.Font(os.path.join('src','assets', 'fonts', 'Karasha.ttf'), 100)
        self.display = display
        self.display.blit(fundo, (0, 0))
        text = font.render('Space Ninjas With Attitude', True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (self.display.get_width()/2, self.display.get_height()/2)
        self.display.blit(text, text_rect)
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
                    nivel = chooseWeapon.chooseWeapon(self.display)
                    nivel.desenha(self.display)
                    while nivel.atualiza_estado():
                        nivel.desenha(self.display)
                    return False
                if self.buttons[1].is_clicked(mouse_pos):
                    return False
        return True
    
    def get_state(self):
        return self.state
    
