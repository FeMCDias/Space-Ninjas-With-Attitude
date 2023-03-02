import pygame
import math
import numpy as np

# Classe que define os atributos de um planeta, esse é o nosso atrator gravitacional
class Planet():
    def __init__(self, x, y,raio, alcance,c, image):
        self.x = x
        self.y = y
        self.raio = raio
        self.alcance = alcance 
        self.pos = np.array([x, y]) # transforma a posição (x,y) em um array para facilitar os cálculos 
        self.c = c # constante gravitacional
        self.image = image

    def draw_alcance(self, display):
        pygame.draw.circle(display, (255, 255, 255), (self.x, self.y), self.alcance, 1)

    def draw(self, display):
        display.blit(self.image, (self.x-self.raio, self.y-self.raio))
        self.draw_alcance(display)

    def distancia_entre_pontos(self, pos1, pos2):
        return math.sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)
    
    def calcula_gravidade(self,pos_bola, bola_aceleracao, bola_velocidade, height, width, display):
        pos_bola = np.array([pos_bola[0] + width/2, pos_bola[1] + height/2])
        # pygame.draw.line(display, (255, 255, 255), (self.pos[0], self.pos[1]), (pos_bola[0], pos_bola[1]), 1)
        distancia_pontos = self.distancia_entre_pontos(self.pos, pos_bola)
        if distancia_pontos <= self.alcance:
            direcao = self.pos - pos_bola # vetor direção da bola em relação ao planeta

            modulo_vetor = np.linalg.norm(direcao) # módulo do vetor direção, ou seja, a distância entre os dois pontos
            vetor_aceleracao = direcao/ modulo_vetor # vetor com a mesma direção do vetor da direção, porém com módulo 1

            mag_a = self.c / modulo_vetor ** 2 # força gravitacional entre os dois corpos (planeta e bola)

            bola_aceleracao = vetor_aceleracao * mag_a # vetor aceleração da bola
            bola_velocidade = bola_velocidade + bola_aceleracao # velocidade da bola

        return bola_aceleracao, bola_velocidade
    
    def change_level(level, image):
        if level == 1:
            return [Planet(500,250,50,100, 100, image)]
        elif level == 2:
            return [Planet(550,500,50,100, 100, image), Planet(550,250,50,100, 100, image)]
        elif level == 3:
            return [Planet(500,450,50,100, 100, image), Planet(400,350,50,100, 100, image), Planet(600,350,50,100, 100, image),]
        else:
            pass

    # Checa se houve colisão entre a bola e o planeta
    def colisao_bola(self, pos_bola):
          return True if self.distancia_entre_pontos(self.pos, pos_bola) <= self.raio + 100 else False
    
