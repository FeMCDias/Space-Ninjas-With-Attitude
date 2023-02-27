import numpy as np
import pygame as pg
import weapons.weapon as Weapon

class Ball(Weapon.Weapon):
    def __init__(self, nome, level, posicao, screen):
        super().__init__(nome, level)
        self.posicao = posicao
        self.velocidade = np.array([0, 0])
        self.screen = pg.Surface(screen)
        self.status = 'NÃO LANÇADA'
        self.aceleracao = np.array([0.5, 0.5])
        self.pos_centro = self.posicao + np.array([self.screen.get_height()/2, self.screen.get_width()/2])
        self.qtd_lancamentos = 0

    def desenha(self,window):
        rect = pg.Rect(self.posicao, self.screen.get_size())
        self.screen.fill((255,255,255))
        window.blit(self.screen,rect)


    def modulo_vetor(self, vetor):
        return np.linalg.norm(vetor)
    
    def verifica_ammo(self):
        self.qtd_max_lancamentos = super().get_ammo()
        if self.qtd_lancamentos < self.qtd_max_lancamentos:
            return True

    def lancamento(self, pos_mouse):
        if self.status == 'NÃO LANÇADA':
            direcao = np.array([pos_mouse[0] - self.pos_centro[0], pos_mouse[1] - self.pos_centro[1]])
            norm_vetor = self.modulo_vetor(direcao)
            aceleracao = direcao/norm_vetor
            magnitude = abs(aceleracao[0]) + abs(aceleracao[1])
            self.velocidade = np.array([aceleracao[0]/magnitude, aceleracao[1]/magnitude])
        return True
    
    def movimentar_bola(self):
        self.pos = self.posicao + 0.05 * self.velocidade

    def reinicia(self):
        self.posicao = np.array([0, 0])
        self.velocidade = np.array([0, 0])
        self.status = 'NÃO LANÇADA'
        self.qtd_lancamentos = 0

            