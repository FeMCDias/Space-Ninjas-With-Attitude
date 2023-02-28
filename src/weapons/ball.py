import numpy as np
import pygame as pg
import weapons.weapon as Weapon
import math

class Ball(Weapon.Weapon):
    def __init__(self, nome, level, posicao, screen):
        super().__init__(nome, level)
        self.posicao = posicao
        self.velocidade = np.array([0, 0])
        self.screen = pg.Surface(screen)
        self.status = 'NÃO LANÇADA'
        self.aceleracao = np.array([0, 0])
        self.qtd_lancamentos = 0

    def desenha(self,window,assets):
        if self.get_name() == 'katana':
            self.width = 80
            self.height = 80
            window.blit(pg.transform.scale(assets['katana'], (self.width, self.height)), (self.posicao[0], self.posicao[1]))
        elif self.get_name() == 'kunai':
            self.width = 60
            self.height = 60
            window.blit(pg.transform.scale(assets['kunai'], (self.width, self.height)), (self.posicao[0], self.posicao[1]))
        elif self.get_name() == 'shuriken':
            self.width = 30
            self.height = 30
            window.blit(pg.transform.scale(assets['shuriken'], (self.width, self.height)), (self.posicao[0], self.posicao[1]))
        return True
    

    def modulo_vetor(self, vetor):
        return np.linalg.norm(vetor)
    
    # def unit_vector(self, vetor):
    #     return vetor / np.linalg.norm(vetor)
    
    def verifica_ammo(self):
        self.qtd_max_lancamentos = super().get_ammo()
        if self.qtd_lancamentos < self.qtd_max_lancamentos:
            return True
        return False

    def lancamento(self, pos_mouse):
        if self.status == 'NÃO LANÇADA':
            self.direcao = pos_mouse - self.posicao
            self.norm_vetor = self.modulo_vetor(self.direcao)
            self.aceleracao = self.direcao/self.norm_vetor
            self.magnitude = 18
            self.velocidade = self.aceleracao * self.magnitude
            self.status = 'LANÇADA'
            self.qtd_lancamentos += 1
        return True
    
    def atualiza(self):
        if self.status == 'LANÇADA':
            self.posicao = self.movimentar_bola()
        
        return self.posicao
    
    def get_status(self):
        return self.status
    
    def set_status(self, status):
        self.status = status

    def reset_ball(self):
        self.velocidade = np.array([0, 0])
        self.status = 'NÃO LANÇADA'
        self.aceleracao = np.array([0, 0])
        self.qtd_lancamentos = 0

    
    def movimentar_bola(self):
        return self.posicao + 0.1 * self.velocidade

