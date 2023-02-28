import pygame
import pymunk as pm
import math
import os
import numpy as np
import weapons.ball as Ball
import weapons.weapon as Weapon
import obstacles.madeira as Madeira

class level():
    # limitar número de vezes que a classe pode ser instanciada
    __instance_count = 0
    __instance_count_max = 1

    def __init__(self, display, updates) -> None:
        if level.__instance_count < level.__instance_count_max:
            level.__instance_count += 1
            pygame.mixer.init()
            self.valida_lancamento = False
            self.index_ball = 0
            self.window = display
            self.BLACK = (0, 0, 0)
            self.clock = pygame.time.Clock()
            self.FPS = 60  # Frames per Second
            self.level = 1
            #Imagens
            self.assets = {
                # 'catapulta': pygame.image.load(os.path.join('src','assets', 'images', 'catapulta.png')),
                # 'enemy1': pygame.image.load(os.path.join('src','assets', 'images', 'enemy1.png')),
                # 'enemy2': pygame.image.load(os.path.join('src','assets', 'images', 'enemy2.png')),
                # 'enemy3': pygame.image.load(os.path.join('src','assets', 'images', 'enemy3.png')),
                'fundo': pygame.image.load(os.path.join('src','assets', 'images', 'space-ninja-temple.jpg')),
                'katana-ninja': pygame.image.load(os.path.join('src','assets', 'images', 'katana-ninja.png')),
                'katana': pygame.image.load(os.path.join('src','assets', 'images', 'katana.png')),
                'kunai-for-character': pygame.image.load(os.path.join('src','assets', 'images', 'kunai-for-character.png')),
                'kunai-ninja': pygame.image.load(os.path.join('src','assets', 'images', 'kunai-ninja.png')),
                'kunai': pygame.image.load(os.path.join('src','assets', 'images', 'kunai.png')),
                'madeira_left_100': pygame.image.load(os.path.join('src','assets', 'images', 'madeira_left_100.png')),
                'madeira_left_66': pygame.image.load(os.path.join('src','assets', 'images', 'madeira_left_66.png')),
                'madeira_left_33': pygame.image.load(os.path.join('src','assets', 'images', 'madeira_left_33.png')),
                'madeira_left_0': pygame.image.load(os.path.join('src','assets', 'images', 'madeira_left_0.png')),
                'madeira_right_100': pygame.image.load(os.path.join('src','assets', 'images', 'madeira_right_100.png')),
                'madeira_right_66': pygame.image.load(os.path.join('src','assets', 'images', 'madeira_right_66.png')),
                'madeira_right_33': pygame.image.load(os.path.join('src','assets', 'images', 'madeira_right_33.png')),
                'madeira_right_0': pygame.image.load(os.path.join('src','assets', 'images', 'madeira_right_0.png')),
                'ninja-main': pygame.image.load(os.path.join('src','assets', 'images', 'ninja-main.png')),
                'shuriken-ninja': pygame.image.load(os.path.join('src','assets', 'images', 'shuriken-ninja.png')),
                'shuriken': pygame.image.load(os.path.join('src','assets', 'images', 'shuriken.png')),
                # 'spikeball': pygame.image.load(os.path.join('src','assets', 'images', 'spikeball.png'))
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
            self.pos_mouse = pygame.mouse.get_pos()
            # self.balls = [Ball.Ball(self.state['weapon'],self.level,[50,50], [1220,650]) for i in range(self.state['ammo'])]
            if self.state['weapon'] == 'katana':
                self.posicao_inicial = np.array((237, 487))
            elif self.state['weapon'] == 'kunai':
                self.posicao_inicial = np.array((237, 535))
            elif self.state['weapon'] == 'shuriken':
                self.posicao_inicial = np.array((237, 550))
            self.ball = Ball.Ball(self.state['weapon'],self.level,self.posicao_inicial, [1220,650])
            self.madeiras_sprite = self.cria_sprites_e_madeiras(5)
    
    def cria_sprites_e_madeiras(self, qtd_madeiras):
        madeiras_sprite = pygame.sprite.Group()
        madeiras = [Madeira.MadeiraSprite('left', 500 + 300*i, 420, 100) for i in range(qtd_madeiras//2)] + [Madeira.MadeiraSprite('right', 600 + 300*i, 420, 100) for i in range(qtd_madeiras//2)]
        for madeira in madeiras:
            madeiras_sprite.add(madeira)
        return madeiras_sprite
    
    def atualiza_sprites_e_madeiras(self, madeiras_sprite):
        for madeira in madeiras_sprite:
            if self.colisao_quadrados(self.ball.posicao[0], self.ball.posicao[1],self.ball.width, self.ball.height, madeira.x, madeira.y, 50, 100) and not madeira.morta:
                madeira.set_life(madeira.vida - self.ball.damage)
                if madeira.vida <= 0:
                    madeira.morta = True
                else:
                    self.ball.set_status("NÃO LANÇADA")
                    self.ball.posicao = self.posicao_inicial
            

    def desenha(self,display): 
        self.window = display
        self.window.fill((0, 0, 0))
        self.window.blit(self.assets['fundo'], (0, 0))
        #Bolas
        # self.ball.desenha(self.window,color=(255,0,0))
        # for i in range(self.index_ball +1):
            # current_ball = self.balls[i]
            # current_ball.desenha(self.window)
            
        self.window.blit(pygame.transform.scale(self.assets['ninja-main'], (67, 100)), (180, 500))
        if not self.ball.get_status():
            if self.state['weapon'] == 'katana':
                self.window.blit(pygame.transform.scale(self.assets['katana'], (80, 80)), (237, 487))
            elif self.state['weapon'] == 'kunai':
                self.window.blit(pygame.transform.scale(self.assets['kunai'], (60, 60)), (237, 535))
            elif self.state['weapon'] == 'shuriken':
                self.window.blit(pygame.transform.scale(self.assets['shuriken'], (30, 30)), (237, 550))
            
        self.ball.desenha(self.window, self.assets)
        
        for sprite in self.madeiras_sprite:
            sprite.render(self.window, self.assets)
        self.atualiza_sprites_e_madeiras(self.madeiras_sprite)
        
        pygame.display.update()
    
    def confere_vitoria_derrota(self):
        pass
    #     if self.state['vitoria']:
    #         return 'vitoria'
    #     elif self.state['derrota']:
    #         return 'derrota'
    #     else:
    #         return None
    def distancia(self, x1, y1, x2, y2):
        return math.sqrt((x1-x2)**2 + (y1-y2)**2)
    
    def roda_musica(self, porcentagem, assets, state):
        state['relogio_musica'].tick()
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        pygame.mixer.music.load(assets['NOME DA MÚSICA'])
        pygame.mixer.music.set_volume(0.9)
        pygame.mixer.music.play()
        state['nome_musica_tocando'] = 'NOME DA MÚSICA'

    def colisao_quadrados(self, x1, y1, w1, h1, x2, y2, w2, h2):
        if x1 > x2 + w2 or x1 + w1 < x2 or y1 > y2 + h2 or y1 + h1 < y2:
            return False
        else:
            return True

    def atualiza_estado(self):
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                return False
            # elif ev.type == pygame.MOUSEBUTTONDOWN:
                # if self.balls[self.index_ball].verifica_ammo():
                #     self.balls[self.index_ball].lancamento(pygame.mouse.get_pos())
                #     self.index_ball += 1
                # pass
            elif ev.type == pygame.MOUSEBUTTONDOWN:
                 if self.ball.verifica_ammo():
                    self.ball.lancamento(pygame.mouse.get_pos())
                    
        # Atualiza a posição da bola
        self.ball.atualiza()    

        return True

    def gameloop(self):
        while self.atualiza_estado():
            self.desenha(self.window)


    def finaliza(self):
        pygame.quit()
