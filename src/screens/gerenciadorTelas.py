# classe que irá gerenciar as telas do jogo

import pygame
import screens.chooseWeapon as chooseWeapon
import screens.home as home
import screens.derrota as derrota
import screens.vitoria as vitoria
import screens.tuto as tuto
import fases.level
import os

# Classe que é responsável por gerenciar as telas do jogo, recebendo argumentos necessários para a inicialização de cada tela
# Além de facilitar de "passar" informações entre as telas
class GerenciadorTelas():
    def __init__(self, display,updates={}, restart=False):
        self.display = display
        self.current_screen_string = 'home'
        self.updates = updates
        self.previous_screen = ['home']
        self.restart = restart
    
    # Função que irá atualizar a tela atual de acordo com o estado atual do jogo (definido de acordo com os cliques do usuário)
    def atualiza(self):
        if self.current_screen_string == 'home' :
            self.current_screen = home.Home(self.display)
            self.previous_screen.append('home')
        elif self.current_screen_string == 'tuto':
            self.current_screen = tuto.Tuto(self.display)
            self.previous_screen.append('tuto')
        elif (self.current_screen_string == 'chooseWeapon' and self.previous_screen[-1] != 'chooseWeapon') or self.restart:
            self.current_screen = chooseWeapon.chooseWeapon(self.display)
            self.previous_screen.append('chooseWeapon')
        elif (self.current_screen_string == 'level' and self.previous_screen[-1] != 'level') or self.restart:
            self.current_screen = fases.level.level(self.display, self.updates)
            self.previous_screen.append('level')
        elif self.current_screen_string == 'derrota' and self.previous_screen[-1] != 'derrota':
            pygame.mixer.music.stop()
            pygame.mixer.music.load(os.path.join('src','assets', 'music', 'Beneath_the_Mask.mp3'))
            pygame.mixer.music.play(-1)
            self.current_screen = derrota.Derrota(self.display)
            self.previous_screen.append('derrota')
        elif self.current_screen_string == 'vitoria' and self.previous_screen[-1] != 'vitoria':
            pygame.mixer.music.stop()
            pygame.mixer.music.load(os.path.join('src','assets', 'music', 'Beneath_the_Mask.mp3'))
            pygame.mixer.music.play(-1)
            self.current_screen = vitoria.Vitoria(self.display)
            self.previous_screen.append('vitoria')
        return self.current_screen.atualiza_estado()
    
    # Loop principal que sempre irá atualizar a tela atual e desenhá-la de acordo com o estado atual do jogo
    def game_loop(self):
        while self.atualiza():
            self.desenha()

    def set_state(self, next_screen):
        self.current_screen_string = next_screen
        self.game_loop()

    # Função que irá desenhar a tela atual de acordo com o estado atual do jogo
    def desenha(self):
        if self.current_screen_string == 'home' and self.previous_screen[-1] != 'home' :
            self.current_screen = home.Home(self.display)
            self.previous_screen.append('home')
        elif self.current_screen_string == 'chooseWeapon' and self.previous_screen[-1] != 'chooseWeapon':
            self.current_screen = chooseWeapon.chooseWeapon(self.display)
            self.previous_screen.append('chooseWeapon')
        elif self.current_screen_string == 'level' and self.previous_screen[-1] != 'level':
            self.current_screen = fases.level.level(self.display, self.updates)
            self.previous_screen.append('level')
        elif self.current_screen_string == 'derrota' and self.previous_screen[-1] != 'derrota':
            self.current_screen = derrota.Derrota(self.display)
            self.previous_screen.append('derrota')
        elif self.current_screen_string == 'vitoria' and self.previous_screen[-1] != 'vitoria':
            self.current_screen = vitoria.Vitoria(self.display)
            self.previous_screen.append('vitoria')
        self.current_screen.desenha(self.display)

    # Função que irá finalizar o pygame
    def finaliza(self):
        pygame.quit()
