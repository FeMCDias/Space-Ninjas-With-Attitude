import pygame
from interface import *
from weapons.weapon import *
import fases.level as level
import os

class chooseWeapon:
    def __init__(self, display):
        font = pygame.font.Font(os.path.join('src','assets', 'fonts', 'Karasha.ttf'), 50)
        self.display = display
        self.buttons = []
        self.buttons.append(Button(100, 100, 200, 100, None, (255, 0, 0), font, (0, 0, 0), 30))
        self.buttons[0].add_text('Katana')
        self.buttons.append(Button(100, 300, 200, 100, None, (255, 0, 0), font, (0, 0, 0), 30))
        self.buttons[1].add_text('Shuriken')
        self.buttons.append(Button(100, 500, 200, 100, None, (255, 0, 0), font, (0, 0, 0), 30))
        self.buttons[2].add_text('Kunai')
        self.state = {}
        self.level = 1

    def desenha(self, display):
        katana_ninja = pygame.image.load(os.path.join('src','assets', 'images', 'katana-ninja.png'))
        shuriken_ninja = pygame.image.load(os.path.join('src','assets', 'images', 'shuriken-ninja.png'))
        kunai_ninja = pygame.image.load(os.path.join('src','assets', 'images', 'kunai-ninja.png'))
        fundo = pygame.image.load(os.path.join('src','assets', 'images', 'space-ninja-temple.jpg'))
        self.display.blit(fundo, (0, 0))
        self.display = display
        for button in self.buttons:
            pygame.draw.rect(self.display, (255, 255, 255), (button.x-5, button.y-5, button.w+10, button.h+10), 5, border_radius=35)
            button.draw(self.display)
        # scale during blit
        katana_ninja = pygame.transform.scale(katana_ninja, (118, 110))
        shuriken_ninja = pygame.transform.scale(shuriken_ninja, (76, 110))
        kunai_ninja = pygame.transform.scale(kunai_ninja, (115, 90))
        self.display.blit(katana_ninja, (350, 95))
        self.display.blit(shuriken_ninja, (350, 295))
        self.display.blit(kunai_ninja, (350, 500))
        pygame.display.update()

    def atualiza_estado(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = False
                mouse_pos = pygame.mouse.get_pos()
                if self.buttons[0].is_clicked(mouse_pos):
                    self.state['weapon'] = Weapon('katana',self.level)
                    clicked = True
                if self.buttons[1].is_clicked(mouse_pos):
                    self.state['weapon'] = Weapon('shuriken',self.level)
                    clicked = True
                if self.buttons[2].is_clicked(mouse_pos):
                    self.state['weapon'] = Weapon('kunai',self.level)
                    clicked = True
                if clicked:
                    nivel = level.level() 
                    nivel.state.update({'weapon': self.state['weapon'].name,
                                    'amount': self.state['weapon'].ammo})
                    window, assets, state = nivel.inicializa()
                    nivel.gameloop(window, assets, state)
                    nivel.finaliza()
        return True
    
    def get_state(self):
        return self.state