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
        self.qtd_lancamentos = 0


    def desenha(self,window):
        print(self.posicao)
        rect = pg.Rect(self.posicao, [20,20])
        pg.draw.rect(window, (255,255,255), rect)
        return True
    

    def modulo_vetor(self, vetor):
        return np.linalg.norm(vetor)
    
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
            magnitude = abs(direcao)
            self.velocidade = aceleracao * magnitude
            self.status = 'LANÇADA'
            self.qtd_lancamentos += 1
        return True
    
    def atualiza(self):
        if self.status == 'LANÇADA':
            self.posicao = self.movimentar_bola()
            print(self.posicao)
        
        return self.posicao
    
    def movimentar_bola(self):
        return self.posicao + 0.2 * self.velocidade

            