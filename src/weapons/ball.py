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

    def desenha(self,window,color = (255, 255, 255)):
        print(self.posicao)
        rect = pg.Rect(self.posicao, [20,20])
        pg.draw.rect(window, color , rect)


    def modulo_vetor(self, vetor):
        return np.linalg.norm(vetor)
    
    def verifica_ammo(self):
        self.qtd_max_lancamentos = super().get_ammo()
        if self.qtd_lancamentos < self.qtd_max_lancamentos:
            return True
        return False

    def lancamento(self, pos_mouse):
        if self.status == 'NÃO LANÇADA':
            direcao = np.array([pos_mouse[0] - self.pos_centro[0], pos_mouse[1] - self.pos_centro[1]])
            norm_vetor = self.modulo_vetor(direcao)
            aceleracao = direcao/norm_vetor
            magnitude = abs(direcao)
            self.velocidade = aceleracao * magnitude
            self.status = 'LANÇADA'
            self.qtd_lancamentos += 1
        return True
    
    def atualiza(self):
        if self.status == 'LANÇADA':
            self.movimentar_bola()
            if self.posicao[0] < 0 or self.posicao[0] > self.screen.get_width():
                self.reinicia()
            if self.posicao[1] < 0 or self.posicao[1] > self.screen.get_height():
                self.reinicia()
    
    def movimentar_bola(self):
        self.posicao = self.posicao + 0.11 * self.velocidade

    def reinicia(self):
        self.posicao = np.array([0, 0])
        self.velocidade = np.array([0, 0])
        self.status = 'NÃO LANÇADA'
        self.qtd_lancamentos = 0

            