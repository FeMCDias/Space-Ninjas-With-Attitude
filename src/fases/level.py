import pygame
import pymunk as pm
import math
import os
import numpy as np
import weapons.ball as Ball
import weapons.weapon as Weapon
import obstacles.madeira as Madeira
import screens.gerenciadorTelas as gerenciadorTelas

class level():
    # limitar número de vezes que a classe pode ser instanciada
    __instance_count = 0
    __instance_count_max = 1

    def __init__(self, display, updates) -> None:
        self.next_screen = 'derrota'
        if level.__instance_count < level.__instance_count_max:
            level.__instance_count += 1
            pygame.mixer.init()
            self.window = display
            self.BLACK = (0, 0, 0)
            self.clock = pygame.time.Clock()
            self.FPS = 60  # Frames per Second
            self.level = 1
            self.victory = False
            #Imagens
            self.assets = {
                # 'catapulta': pygame.image.load(os.path.join('assets', 'images', 'catapulta.png')),
                # 'enemy1': pygame.image.load(os.path.join('assets', 'images', 'enemy1.png')),
                # 'enemy2': pygame.image.load(os.path.join('assets', 'images', 'enemy2.png')),
                # 'enemy3': pygame.image.load(os.path.join('assets', 'images', 'enemy3.png')),
                'fundo': pygame.image.load(os.path.join('assets', 'images', 'space-ninja-temple.jpg')),
                'katana-ninja': pygame.image.load(os.path.join('assets', 'images', 'katana-ninja.png')),
                'katana': pygame.transform.scale(pygame.image.load(os.path.join('assets', 'images', 'katana.png')),(80,80)),
                'kunai-for-character': pygame.image.load(os.path.join('assets', 'images', 'kunai-for-character.png')),
                'kunai-ninja': pygame.image.load(os.path.join('assets', 'images', 'kunai-ninja.png')),
                'kunai': pygame.transform.scale(pygame.image.load(os.path.join('assets', 'images', 'kunai.png')),(60,60)),
                'madeira_left_100': pygame.transform.scale(pygame.image.load(os.path.join('assets', 'images', 'madeira_left_100.png')),(100, 200)),
                'madeira_left_66': pygame.transform.scale(pygame.image.load(os.path.join('assets', 'images', 'madeira_left_66.png')),(100, 200)),
                'madeira_left_33': pygame.transform.scale(pygame.image.load(os.path.join('assets', 'images', 'madeira_left_33.png')),(100, 200)),
                'madeira_left_0': pygame.transform.scale(pygame.image.load(os.path.join('assets', 'images', 'madeira_left_0.png')),(100, 200)),
                'madeira_left_rotate' : pygame.transform.scale(pygame.image.load(os.path.join('assets', 'images', 'madeira_left_0_rotate.png')),(200, 100)),
                'madeira_right_100': pygame.transform.scale(pygame.image.load(os.path.join('assets', 'images', 'madeira_right_100.png')),(100, 200)),
                'madeira_right_66': pygame.transform.scale(pygame.image.load(os.path.join('assets', 'images', 'madeira_right_66.png')),(100, 200)),
                'madeira_right_33': pygame.transform.scale(pygame.image.load(os.path.join('assets', 'images', 'madeira_right_33.png')),(100, 200)),
                'madeira_right_0': pygame.transform.scale(pygame.image.load(os.path.join('assets', 'images', 'madeira_right_0.png')),(100, 200)),
                'madeira_right_rotate' : pygame.transform.scale(pygame.image.load(os.path.join('assets', 'images', 'madeira_right_0_rotate.png')),(200, 100)),
                'ninja-main': pygame.image.load(os.path.join('assets', 'images', 'ninja-main.png')),
                'shuriken-ninja': pygame.image.load(os.path.join('assets', 'images', 'shuriken-ninja.png')),
                'shuriken': pygame.transform.scale(pygame.image.load(os.path.join('assets', 'images', 'shuriken.png')),(60,60)),
                # 'spikeball': pygame.image.load(os.path.join('assets', 'images', 'spikeball.png'))
            }

            
            self.state = {
                'atirando': False,
                'atirou': False,
                'quitou': False,
                'bola':{
                    'center': (0, 0),
                }
            }

            self.state.update(updates) #Atualiza o dicionário de estados com as informações passadas da tela anterior (chooseWeapon)    
            if self.state['weapon'] == 'katana':
                self.posicao_inicial = np.array((237, 487))
            elif self.state['weapon'] == 'kunai':
                self.posicao_inicial = np.array((237, 535))
            elif self.state['weapon'] == 'shuriken':
                self.posicao_inicial = np.array((237, 550))
            self.ball = Ball.Ball(self.state['weapon'],self.level,self.posicao_inicial, [1220,650])
            self.madeiras_sprite = self.cria_sprites_e_madeiras(2)
    
    def cria_sprites_e_madeiras(self, qtd_madeiras):
        madeiras_sprite = pygame.sprite.Group()
        madeiras = [Madeira.MadeiraSprite('left', 450 + 400*i, 420, 100) for i in range(qtd_madeiras//2)] + [Madeira.MadeiraSprite('right', 650 + 400*i, 420, 100) for i in range(qtd_madeiras//2)]
        for madeira in madeiras:
            madeiras_sprite.add(madeira)
        return madeiras_sprite
    
    def atualiza_sprites_e_madeiras(self, madeiras_sprite):
        for madeira in madeiras_sprite:
            if not madeira.morta:
                if self.colisao_quadrados(self.ball.posicao[0], self.ball.posicao[1],self.ball.width, self.ball.height, madeira.x, madeira.y, 50, 100):
                    madeira.set_life(madeira.vida - self.ball.damage)
                    if madeira.vida <= 0:
                        madeira.morta = True
                    else:
                        # self.ball.set_status("NÃO LANÇADA")
                        self.ball.posicao = self.posicao_inicial
                        self.ball.ammo -= 1
                        self.ball.reset_ball()
                if madeira.check_in_orbit(self.ball.posicao):
                    ball_to_madeira = madeira.get_center() - self.ball.posicao
                    ball_to_madeira = ball_to_madeira / np.linalg.norm(ball_to_madeira)
                    #change ball velocity according to the madeira
                    # self.ball.aceleracao = madeira.gravidade*0.01/ball_to_madeira**2 
                    # self.ball.velocidade = self.ball.velocidade + self.ball.aceleracao
                    # self.ball.posicao = self.ball.posicao - ball_to_madeira
                
    def checa_saiu_tela(self):
        if self.ball.posicao[0] < 0 or self.ball.posicao[0] > 1280 or self.ball.posicao[1] < 0 or self.ball.posicao[1] > 720:
            self.ball.reset_ball()
            self.ball.ammo -= 1
            self.ball.posicao = self.posicao_inicial
            

    def desenha(self,display): 
        self.window = display
        self.window.fill((0, 0, 0))
        self.window.blit(self.assets['fundo'], (0, 0))
            
        self.window.blit(pygame.transform.scale(self.assets['ninja-main'], (67, 100)), (180, 500))
        if not self.ball.get_status():
            if self.state['weapon'] == 'katana':
                self.window.blit(self.assets['katana'], (80, 80), (237, 487))
            elif self.state['weapon'] == 'kunai':
                self.window.blit(self.assets['kunai'], (60, 60), (237, 535))
            elif self.state['weapon'] == 'shuriken':
                self.window.blit(self.assets['shuriken'], (30, 30), (237, 550))
        
        # blit text with weapon count
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("Shots left: " + str(self.ball.ammo), True, (255, 255, 255))
        self.window.blit(text, (1000, 50))
        
        for sprite in self.madeiras_sprite:
            sprite.render(self.window, self.assets)
        self.ball.desenha(self.window, self.assets)
        self.atualiza_sprites_e_madeiras(self.madeiras_sprite)
        self.checa_saiu_tela()
        
        pygame.display.update()
        
    def distancia(self, x1, y1, x2, y2):
        return math.sqrt((x1-x2)**2 + (y1-y2)**2)
    
    # def roda_musica(self, porcentagem, assets, state):
    #     state['relogio_musica'].tick()
    #     pygame.mixer.music.stop()
    #     pygame.mixer.music.unload()
    #     pygame.mixer.music.load(assets['NOME DA MÚSICA'])
    #     pygame.mixer.music.set_volume(0.9)
    #     pygame.mixer.music.play()
    #     state['nome_musica_tocando'] = 'NOME DA MÚSICA'

    def colisao_quadrados(self, x1, y1, w1, h1, x2, y2, w2, h2):
        if x1 > x2 + w2 or x1 + w1 < x2 or y1 > y2 + h2 or y1 + h1 < y2:
            return False
        else:
            return True

    def atualiza_estado(self):
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                return False
            elif ev.type == pygame.MOUSEBUTTONDOWN:
                 if self.ball.verifica_ammo():
                    self.ball.lancamento(pygame.mouse.get_pos())
        # Atualiza a posição da bola
        self.ball.atualiza()
        if self.ball.ammo <= 0:
            self.next_screen = 'derrota'
            return gerenciadorTelas.GerenciadorTelas(self.window).set_state(self.next_screen)
        elif self.victory:
            self.next_screen = 'vitoria'
            return gerenciadorTelas.GerenciadorTelas(self.window).set_state(self.next_screen)

        return True

    def gameloop(self):
        while self.atualiza_estado():
            self.desenha(self.window)


    def finaliza(self):
        pygame.quit()
