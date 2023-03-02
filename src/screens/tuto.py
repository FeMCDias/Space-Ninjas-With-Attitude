import pygame
from interface import *
import screens.gerenciadorTelas as gerenciadorTelas
import os

# Classe que representa a tela de tutorial, com um botão para continuar e outro para sair
class Tuto:
    def __init__(self, display):
        font = pygame.font.Font(os.path.join('src','assets', 'fonts', 'Karasha.ttf'), 50)
        self.next_screen = 'chooseWeapon'
        self.screen_name = 'tuto'
        self.display = display
        self.buttons = []
        self.buttons.append(Button(250, 500, 320, 100, None, (255, 0, 0), font, (0, 0, 0),30))
        self.buttons[0].add_text('I understand')
        self.buttons.append(Button(self.buttons[0].x + self.buttons[0].w + 150, self.buttons[0].y, 200, 100, None, (255, 0, 0), font, (0, 0, 0), 30))
        self.buttons[1].add_text('Quit')
        self.state = {}
        self.fundo = pygame.image.load(os.path.join('src','assets', 'images', 'space-ninja-temple.jpg'))
        self.title_font = pygame.font.Font(os.path.join('src','assets', 'fonts', 'Karasha.ttf'), 100)
        self.font = pygame.font.Font(os.path.join('src','assets', 'fonts', 'Karasha.ttf'), 40)
        self.enemies = {
            'enemy1':pygame.transform.scale(pygame.image.load(os.path.join('src','assets', 'images', 'enemy1.png')), (113, 150)),
            'enemy2':pygame.transform.scale(pygame.image.load(os.path.join('src','assets', 'images', 'enemy2.png')), (113, 150)),
            'enemy3':pygame.transform.scale(pygame.image.load(os.path.join('src','assets', 'images', 'enemy3.png')), (113, 150)),
                        }
        self.spacecat = pygame.transform.scale(pygame.image.load(os.path.join('src','assets', 'images', 'space_ninja_cat.png')),(150,150))

    # Desenha a tela de tutorial, com um texto explicando como jogar e dois botões para continuar ou sair
    def desenha(self, display):
        self.display = display
        self.display.blit(self.fundo, (0, 0))
        for button in self.buttons:
            pygame.draw.rect(self.display, (255, 255, 255), (button.x-5, button.y-5, button.w+10, button.h+10), 5, border_radius=35)
            button.draw(self.display)

        text = self.title_font.render('Tutorial', True, (255, 255, 255))
        self.display.blit(text, (self.display.get_width()/2 - text.get_width()/2, 50))

        text = self.font.render('Click anywhere on the screen to shoot in that direction', True, (255, 255, 255))
        self.display.blit(text, (self.display.get_width()/2 - text.get_width()/2, 200))

        text = self.font.render('Kill the other space ninjas with limited weapons', True, (255, 200, 200))
        self.display.blit(text, (self.display.get_width()/2 - text.get_width()/2 - 150, 300))

        self.display.blit(self.enemies['enemy1'], (self.display.get_width()/2 - text.get_width()/2 + 690, 250))
        self.display.blit(self.enemies['enemy2'], (self.display.get_width()/2 - text.get_width()/2 + 790, 250))
        self.display.blit(self.enemies['enemy3'], (self.display.get_width()/2 - text.get_width()/2 + 890, 250))

        text = self.font.render('Ninja Space Cat will pull your weapon with gravity, be careful...', True, (255, 255, 255))
        self.display.blit(text, (self.display.get_width()/2 - text.get_width()/2, 400))
        self.display.blit(self.spacecat, (self.display.get_width()/2 - text.get_width()/2, 465))
        pygame.display.update()

    # Checa o estado da tela, caso algum botão seja clicado, ele muda o estado da tela
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
    
