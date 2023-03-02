import pygame
from interface import *
import screens.gerenciadorTelas as gerenciadorTelas
import os

# Classe que representa a tela de vitória, com um botão para reiniciar o jogo e outro para sair
class Vitoria:
    def __init__(self, display):
        font = pygame.font.Font(os.path.join('assets', 'fonts', 'Karasha.ttf'), 50)
        self.next_screen = 'chooseWeapon'
        self.screen_name = 'vitoria'
        self.display = display
        self.buttons = []
        self.buttons.append(Button(400, 450, 200, 100, None, (255, 0, 0), font, (0, 0, 0),30))
        self.buttons[0].add_text('Restart')
        self.buttons.append(Button(self.buttons[0].x + self.buttons[0].w + 50, self.buttons[0].y, 200, 100, None, (255, 0, 0), font, (0, 0, 0), 30))
        self.buttons[1].add_text('Quit')
        self.state = {}

    # Desenha a tela de vitória
    def desenha(self, display):
        fundo = pygame.image.load(os.path.join('assets', 'images', 'back_victory.jpg'))
        self.display = display
        self.display.blit(fundo, (0, 0))
        for button in self.buttons:
            pygame.draw.rect(self.display, (255, 255, 255), (button.x-5, button.y-5, button.w+10, button.h+10), 5, border_radius=35)
            button.draw(self.display)
        pygame.display.update()

    # Atualiza o estado da tela de vitória, caso o botão de reiniciar o jogo seja clicado, o jogo é reiniciado
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
    
