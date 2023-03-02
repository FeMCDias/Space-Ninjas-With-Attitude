import numpy as np
import pygame as pg
import weapons.weapon as Weapon

# Classe que herda os atributos da classe "Weapon" e define os atributos específicos de uma bola
class Ball(Weapon.Weapon):
    def __init__(self, nome, level, posicao, screen):
        super().__init__(nome, level)
        self.posicao = posicao
        self.velocidade = np.array([0, 0])
        self.screen = pg.Surface(screen)
        self.status = 'NÃO LANÇADA'
        self.aceleracao = np.array([0, 0])
        self.qtd_lancamentos = 0
        self.existe = True

    # Desenha a bola na tela (com sua "skin" específica) e atualiza sua posição, por causa do tipo de arma")
    def desenha(self,window,assets):
        if self.get_name() == 'katana':
            self.width = 80
            self.height = 80
            window.blit(assets['katana'], (self.posicao[0], self.posicao[1]))
        elif self.get_name() == 'kunai':
            self.width = 60
            self.height = 60
            window.blit(assets['kunai'], (self.posicao[0], self.posicao[1]))
        elif self.get_name() == 'shuriken':
            self.width = 30
            self.height = 30
            window.blit(assets['shuriken'], (self.posicao[0], self.posicao[1]))
        return True
    
    # Auxilia ao calcular o módulo de um vetor
    def modulo_vetor(self, vetor):
        return np.linalg.norm(vetor)
    
    # Checa se a bola ainda pode ser lançada, de acordo com a quantidade de lançamentos que ela pode fazer
    def verifica_ammo(self):
        self.qtd_max_lancamentos = super().get_ammo()
        if self.qtd_lancamentos < self.qtd_max_lancamentos:
            return True
        return False

    # Define a direção e a velocidade da bola, de acordo com a posição do mouse
    def lancamento(self, pos_mouse):
        if self.status == 'NÃO LANÇADA':
            self.direcao = pos_mouse - self.posicao # Direção da bola
            self.norm_vetor = self.modulo_vetor(self.direcao) # Módulo da direção
            self.aceleracao = self.direcao/self.norm_vetor # Aceleração da bola
            self.magnitude = 5 # Força da bola
            self.velocidade = self.aceleracao * self.magnitude # Nova velocidade da bola
            self.status = 'LANÇADA'
            self.qtd_lancamentos += 1
        return True
    
    def atualiza(self):
        if self.status == 'LANÇADA':
            self.posicao = self.movimentar_bola() # Atualiza a posição da bola
        
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

    def set_aceleracao(self, aceleracao):
        self.aceleracao = aceleracao

    # Define a posição da bola, de acordo com a velocidade e a aceleração
    def movimentar_bola(self):
        return self.posicao + 0.1 * self.velocidade

