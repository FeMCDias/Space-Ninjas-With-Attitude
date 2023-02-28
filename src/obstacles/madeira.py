import pygame
import numpy as np


class MadeiraSprite(pygame.sprite.Sprite):
    def __init__(self, type, x, y, vida=100, gravidade=0.5):
        super().__init__()
        self.type = type
        self.x = x
        self.y = y
        self.vida = vida
        self.image = None
        self.gravidade = gravidade
        self.raio = 200
        self.morta = False
        
        if type == 'left':
            self.image = 'madeira_left_100'
        elif type == 'right':
            self.image = 'madeira_right_100'
            
    def get_center(self):
        return np.array([self.x+50, self.y+100])

    def set_image(self, life, type):
        if type == 'left':
            if life == 100:
                self.image = 'madeira_left_100'
            elif life >= 66:
                self.image = 'madeira_left_66'
            elif life >= 33:
                self.image = 'madeira_left_33'
            elif life >= 0:
                self.image = 'madeira_left_0'
        elif type == 'right':
            if life >= 100:
                self.image = 'madeira_right_100'
            elif life >= 66:
                self.image = 'madeira_right_66'
            elif life >= 33:
                self.image = 'madeira_right_33'
            elif life >= 0:
                self.image = 'madeira_right_0'

    def set_life(self, life):
        self.vida = life
        self.set_image(life, self.type)
    
    def check_in_orbit(self, pos):
        if (pos[0]-self.x-50)**2 + (pos[1]-self.y-100)**2 <= self.raio**2:
            return True
        return False
    
    def render(self, window, assets):
        if not self.morta:
            window.blit(pygame.transform.scale(assets[self.image], (100, 200)), (self.x, self.y))
            pygame.draw.circle(window, (255, 0, 0), (self.x+50, self.y+100), self.raio, 1)
        else:
            window.blit(pygame.transform.scale(pygame.transform.rotate(assets[self.image], 90), (200, 100)), (self.x, self.y+100))