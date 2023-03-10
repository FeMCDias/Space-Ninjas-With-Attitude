import pygame
# Classe que representa um botão, com um texto e uma cor. Auxilia na criação de menus e telas
class Button:
    def __init__(self, x, y, w, h, text, color, font, font_color, radius=-1):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.text = text
        self.text_pos = None
        self.color = color
        self.font = font
        self.font_color = font_color
        self.radius = radius

    # Adiciona um texto ao botão
    def add_text(self, text, size = 25, text_color = (0, 0, 0)):
        if self.font == None:
            self.font = pygame.font.SysFont('Arial', size)
        self.text = self.font.render(text, True, text_color)
        self.text_pos = self.text.get_rect()

    # Desenha o botão na tela com o texto
    def draw(self, display):
        pygame.draw.rect(display, self.color, (self.x, self.y, self.w, self.h), border_radius=self.radius)
        self.text_pos.center = (self.x + self.w/2, self.y + self.h/2)
        display.blit(self.text, self.text_pos)

    # Checa se o botão foi clicado, retornando True ou False
    def is_clicked(self, mouse_pos):
        if mouse_pos[0] > self.x and mouse_pos[0] < self.x + self.w and mouse_pos[1] > self.y and mouse_pos[1] < self.y + self.h:
            return True
        else:
            return False
        


