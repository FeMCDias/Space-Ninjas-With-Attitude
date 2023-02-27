import numpy as np
import pygame as pg
import weapons.weapon as Weapon

class Ball(Weapon.Weapon):
    def __init__(self, posicao, screen, level, name):
        super().__init__(name, level)
        self.posicao = posicao
        self.velocidade = np.array([0, 0])
        self.screen = pg.Surface(screen)
        self.status = 'NÃO LANÇADA'
        self.aceleracao = np.array([0.5, 0.5])
        self.pos_centro = self.posicao + np.array([self.screen.get_height()/2, self.screen.get_width()/2])
        self.qtd_lancamentos = 0

    def desenha(self):
        pg.draw.circle(self.screen, (255, 255, 255), self.posicao, 10)


    def modulo_vetor(self, vetor):
        return np.linalg.norm(vetor)
    
    def verifica_ammo(self):
        self.qtd_max_lancamentos = super().get_ammo()
        if self.qtd_lancamentos < self.qtd_max_lancamentos:
            return True

    def lancamento(self, attempt, pos_mouse):
        if self.status == 'NÃO LANÇADA':
            direcao = np.array([pos_mouse[0] - self.pos_centro[0], pos_mouse[1] - self.pos_centro[1]])
            norm_vetor = self.modulo_vetor(direcao)
            aceleracao = np.array([direcao[0]/norm_vetor, direcao[1]/norm_vetor])
            magnitude = abs(direcao[0]) + abs(direcao[1])
            self.velocidade = np.array([aceleracao[0]*magnitude, aceleracao[1]*magnitude])
    
    def movimento(self):
        self.pos = self.posicao * 0.1 + self.velocidade

    def reinicia(self):
        self.posicao = np.array([0, 0])
        self.velocidade = np.array([0, 0])
        self.status = 'NÃO LANÇADA'
        self.qtd_lancamentos = 0

            