import pygame
import numpy as np

# Classe que cria uma madeira que é responsável por atrapalhar o jogador (um obstáculo)
# Essa utiliza Sprite, que é uma classe do pygame que facilita a criação de objetos que se movem
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

    # Setta a imagem da madeira de acordo com a vida que ela tem
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
            elif life <= 0:
                self.image = 'madeira_left_rotate'
        elif type == 'right':
            if life >= 100:
                self.image = 'madeira_right_100'
            elif life >= 66:
                self.image = 'madeira_right_66'
            elif life >= 33:
                self.image = 'madeira_right_33'
            elif life > 0:
                self.image = 'madeira_right_0'
            elif life <= 0:
                self.image = 'madeira_right_rotate'

    # Setta a vida da madeira
    def set_life(self, life):
        self.vida = life
        self.set_image(life, self.type)
    
    # Verifica se a madeira está morta ou não, se estiver, ela cai
    def render(self, window, assets):
        if not self.morta:
            window.blit(assets[self.image], (self.x, self.y))
        else:
            window.blit(assets[self.image], (self.x, self.y+100))