import pygame
from interface import *
from weapons.weapon import *
import levels.level as level

class chooseWeapon:
    def __init__(self, display):
        self.display = display
        self.buttons = []
        self.buttons.append(Button(100, 100, 200, 100, None, (255, 0, 0), None, (0, 0, 0)))
        self.buttons[0].add_text('Katana')
        self.buttons.append(Button(100, 300, 200, 100, None, (255, 0, 0), None, (0, 0, 0)))
        self.buttons[1].add_text('Shuriken')
        self.buttons.append(Button(100, 500, 200, 100, None, (255, 0, 0), None, (0, 0, 0)))
        self.buttons[2].add_text('Kunai')
        self.state = {}
        self.level = 1

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
                    self.state['weapon'] = Weapon('katana',self.level)
                if self.buttons[1].is_clicked(mouse_pos):
                    self.state['weapon'] = Weapon('shuriken',self.level)
                if self.buttons[2].is_clicked(mouse_pos):
                    self.state['weapon'] = Weapon('kunai',self.level)
                nivel = level.level() 
                nivel.state.update({'weapon': self.state['weapon'].name,
                                'amount': self.state['weapon'].ammo})
            
                window, assets, state = nivel.inicializa()
                nivel.gameloop(window, assets, state)
                nivel.finaliza()
        return True
    
    def get_state(self):
        return self.state