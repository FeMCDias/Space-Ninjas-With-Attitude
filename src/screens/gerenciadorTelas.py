# classe que irá gerenciar as telas do jogo

import pygame
import screens.chooseWeapon as chooseWeapon
import screens.home as home
import fases.level

class GerenciadorTelas():
    def __init__(self, display,updates={}):
        self.display = display
        self.current_screen = 'home'
        self.updates = updates

    def atualiza(self):
        if self.current_screen == 'home':
            current_screen = home.Home(self.display)
        elif self.current_screen == 'chooseWeapon':
            current_screen = chooseWeapon.chooseWeapon(self.display)
        elif self.current_screen == 'level':
            current_screen = fases.level.level(self.display, self.updates)
        return current_screen.atualiza_estado()
    
    def game_loop(self):
        while self.atualiza():
            self.desenha()

    def set_state(self, next_screen):
        self.current_screen = next_screen
        self.game_loop()


    def desenha(self):
        if self.current_screen == 'home':
            current_screen = home.Home(self.display)
        elif self.current_screen == 'chooseWeapon':
            current_screen = chooseWeapon.chooseWeapon(self.display)
        elif self.current_screen == 'level':
            current_screen = fases.level.level(self.display, self.updates) #updates são as atualizações provindas da tela anterior (chooseWeapon) e que serão passadas para a próxima tela (level)	
        current_screen.desenha(self.display)


    def finaliza(self):
        pygame.quit()
