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
        self.screen_name = 'chooseWeapon'
        self.display = display
        self.buttons = []
        self.buttons.append(Button(100, 50, 200, 100, None, (255, 0, 0), font, (0, 0, 0), 30))
        self.buttons[0].add_text('Katana')
        self.buttons.append(Button(100, 250, 200, 100, None, (255, 0, 0), font, (0, 0, 0), 30))
        self.buttons[1].add_text('Shuriken')
        self.buttons.append(Button(100, 450, 200, 100, None, (255, 0, 0), font, (0, 0, 0), 30))
        self.buttons[2].add_text('Kunai')
        self.state = {}
        self.level = 1
        self.clicked = False
        self.ninjas = {
            'katana_ninja':pygame.transform.scale( pygame.image.load(os.path.join( 'assets', 'images', 'katana-ninja.png')), (118, 110)),
            'shuriken_ninja':pygame.transform.scale( pygame.image.load(os.path.join( 'assets', 'images', 'shuriken-ninja.png')), (76, 110)),
            'kunai_ninja':pygame.transform.scale( pygame.image.load(os.path.join( 'assets', 'images', 'kunai-ninja.png')), (115, 90))}
        self.fundo = pygame.image.load(os.path.join( 'assets', 'images', 'space-ninja-temple.jpg'))
        self.font = pygame.font.SysFont('Bauhaus 93', 30)
    def desenha(self, display):
        self.display.blit(self.fundo, (0, 0))
        self.display = display

        for button in self.buttons:
            pygame.draw.rect(self.display, (255, 255, 255), (button.x-5, button.y-5, button.w+10, button.h+10), 5, border_radius=35)
            button.draw(self.display)

        self.display.blit(self.ninjas['katana_ninja'], (350, 45))
        self.display.blit(self.ninjas['shuriken_ninja'], (350, 245))
        self.display.blit(self.ninjas['kunai_ninja'], (350, 455))

        self.display.blit(self.font.render('Damage: 75', True, (255, 255, 255)), (100, 170))
        self.display.blit(self.font.render('Ammo: 2 + 2 p/ level', True, (255, 255, 255)), (100, 200)) 
        self.display.blit(self.font.render('Damage: 50', True, (255, 255, 255)), (100, 370))
        self.display.blit(self.font.render('Ammo: 4 + 2 p/ level', True, (255, 255, 255)), (100, 400))
        self.display.blit(self.font.render('Damage: 66', True, (255, 255, 255)), (100, 570))
        self.display.blit(self.font.render('Ammo: 3 + 2 p/ level', True, (255, 255, 255)), (100, 600))

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