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
        self.aceleracao = np.array([0.5, 0.5])
        self.qtd_lancamentos = 0


    def desenha(self,window,assets):
        if self.get_name() == 'katana':
            window.blit(pg.transform.scale(assets['katana'], (80, 80)), (self.posicao[0], self.posicao[1]))
        elif self.get_name() == 'kunai':
            window.blit(pg.transform.scale(assets['kunai'], (60, 60)), (self.posicao[0], self.posicao[1]))
        elif self.get_name() == 'shuriken':
            window.blit(pg.transform.scale(assets['shuriken'], (30, 30)), (self.posicao[0], self.posicao[1]))
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
            direcao = np.array(pos_mouse) - self.posicao
            norm_vetor = self.modulo_vetor(direcao)
            aceleracao = direcao/norm_vetor
            magnitude = 5
            self.velocidade = aceleracao * magnitude
            self.status = 'LANÇADA'
            self.qtd_lancamentos += 1
        return True
    
    def atualiza(self):
        if self.status == 'LANÇADA':
            self.posicao = self.movimentar_bola()
        
        return self.posicao
    
    def get_status(self):
        return self.status
    
    def movimentar_bola(self):
        return self.posicao + 0.1 * self.velocidade

            