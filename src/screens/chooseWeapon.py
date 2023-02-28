import pygame
from interface import *
from weapons.weapon import *
import fases.level as level
import screens.gerenciadorTelas as gerenciadorTelas
import os

class chooseWeapon:
    def __init__(self, display):
        font = pygame.font.Font(os.path.join( 'assets', 'fonts', 'Karasha.ttf'), 50)
        self.next_screen = 'level'
        self.screen_name='chooseWeapon'
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
        self.clicked = False

    def desenha(self, display):
        katana_ninja = pygame.image.load(os.path.join( 'assets', 'images', 'katana-ninja.png'))
        shuriken_ninja = pygame.image.load(os.path.join( 'assets', 'images', 'shuriken-ninja.png'))
        kunai_ninja = pygame.image.load(os.path.join( 'assets', 'images', 'kunai-ninja.png'))
        fundo = pygame.image.load(os.path.join( 'assets', 'images', 'space-ninja-temple.jpg'))
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
                mouse_pos = pygame.mouse.get_pos()
                if self.buttons[0].is_clicked(mouse_pos):
                    self.state['weapon'] = Weapon('katana',self.level)
                    self.clicked = True
                if self.buttons[1].is_clicked(mouse_pos):
                    self.state['weapon'] = Weapon('shuriken',self.level)
                    self.clicked = True
                if self.buttons[2].is_clicked(mouse_pos):
                    self.state['weapon'] = Weapon('kunai',self.level)
                    self.clicked = True
                if self.clicked:
                    updates = self.information_next_screen()
                    return gerenciadorTelas.GerenciadorTelas(self.display,updates).set_state(self.next_screen)
        return True
    
    def get_state(self):
        return self.state
    
    def information_next_screen(self):
        return {
            'weapon': self.state['weapon'].name,
            'ammo': self.state['weapon'].ammo,
        }