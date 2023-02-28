import pygame
from interface import *
import screens.gerenciadorTelas as gerenciadorTelas
import os

class Tuto:
    def __init__(self, display):
        font = pygame.font.Font(os.path.join( 'assets', 'fonts', 'Karasha.ttf'), 50)
        self.next_screen = 'chooseWeapon'
        self.screen_name = 'tuto'
        self.display = display
        self.buttons = []
        self.buttons.append(Button(250, 500, 320, 100, None, (255, 0, 0), font, (0, 0, 0),30))
        self.buttons[0].add_text('I understand')
        self.buttons.append(Button(self.buttons[0].x + self.buttons[0].w + 150, self.buttons[0].y, 200, 100, None, (255, 0, 0), font, (0, 0, 0), 30))
        self.buttons[1].add_text('Quit')
        self.state = {}

    def desenha(self, display):
        fundo = pygame.image.load(os.path.join( 'assets', 'images', 'space-ninja-temple.jpg'))
        font = pygame.font.Font(os.path.join( 'assets', 'fonts', 'Karasha.ttf'), 100)
        self.display = display
        self.display.blit(fundo, (0, 0))
        for button in self.buttons:
            pygame.draw.rect(self.display, (255, 255, 255), (button.x-5, button.y-5, button.w+10, button.h+10), 5, border_radius=35)
            button.draw(self.display)

        text = font.render('Tutorial', True, (255, 255, 255))
        self.display.blit(text, (self.display.get_width()/2 - text.get_width()/2, 50))

        font = pygame.font.Font(os.path.join( 'assets', 'fonts', 'Karasha.ttf'), 40)
        text = font.render('Click anywhere on the screen to shoot in that direction', True, (255, 255, 255))
        self.display.blit(text, (self.display.get_width()/2 - text.get_width()/2, 200))
        text = font.render('Kill the other space ninjas with limited weapons', True, (255, 200, 200))
        self.display.blit(text, (self.display.get_width()/2 - text.get_width()/2 - 150, 300))
        self.display.blit(pygame.transform.scale(pygame.image.load(os.path.join( 'assets', 'images', 'enemy1.png')), (113, 150)), (self.display.get_width()/2 - text.get_width()/2 + 690, 250))
        self.display.blit(pygame.transform.scale(pygame.image.load(os.path.join( 'assets', 'images', 'enemy2.png')), (113, 150)), (self.display.get_width()/2 - text.get_width()/2 + 790, 250))
        self.display.blit(pygame.transform.scale(pygame.image.load(os.path.join( 'assets', 'images', 'enemy3.png')), (113, 150)), (self.display.get_width()/2 - text.get_width()/2 + 890, 250))
        text = font.render('Planets will pull your weapon with gravity, be careful...', True, (255, 255, 255))
        self.display.blit(text, (self.display.get_width()/2 - text.get_width()/2, 400))
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
    
