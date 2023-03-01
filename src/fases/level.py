import pygame
import pymunk as pm
import math
import os
import numpy as np
import weapons.ball as Ball
import weapons.weapon as Weapon
import enemies.enemy as Enemy
import obstacles.madeira as Madeira
import screens.gerenciadorTelas as gerenciadorTelas
import obstacles.planet as Planet

class level():

    def __init__(self, display, updates) -> None:
        self.next_screen = 'derrota'
        self.window = display
        self.level = 1
        self.victory = False
        #Imagens
        self.assets = {
            # 'catapulta': pygame.image.load(os.path.join('src','assets', 'images', 'catapulta.png')),
            'chop_wood': pygame.mixer.Sound(os.path.join('src','assets', 'sounds', 'chop_wood.wav')),
            'cut_enemy_sound': pygame.mixer.Sound(os.path.join('src','assets', 'sounds', 'cut_enemy.wav')),
            'enemy1': pygame.transform.scale(pygame.image.load(os.path.join('src','assets', 'images', 'enemy1.png')),(113,150)),
            'enemy2': pygame.transform.scale(pygame.image.load(os.path.join('src','assets', 'images', 'enemy2.png')),(113,150)),
            'enemy3': pygame.transform.scale(pygame.image.load(os.path.join('src','assets', 'images', 'enemy3.png')),(113,150)),
            'fundo': pygame.image.load(os.path.join('src','assets', 'images', 'space-ninja-temple.jpg')),
            'katana-ninja': pygame.image.load(os.path.join('src','assets', 'images', 'katana-ninja.png')),
            'katana': pygame.transform.scale(pygame.image.load(os.path.join('src','assets', 'images', 'katana.png')),(80,80)),
            'kunai-for-character': pygame.image.load(os.path.join('src','assets', 'images', 'kunai-for-character.png')),
            'kunai-ninja': pygame.image.load(os.path.join('src','assets', 'images', 'kunai-ninja.png')),
            'kunai': pygame.transform.scale(pygame.image.load(os.path.join('src','assets', 'images', 'kunai.png')),(60,60)),
            'madeira_left_100': pygame.transform.scale(pygame.image.load(os.path.join('src','assets', 'images', 'madeira_left_100.png')),(100, 200)),
            'madeira_left_66': pygame.transform.scale(pygame.image.load(os.path.join('src','assets', 'images', 'madeira_left_66.png')),(100, 200)),
            'madeira_left_33': pygame.transform.scale(pygame.image.load(os.path.join('src','assets', 'images', 'madeira_left_33.png')),(100, 200)),
            'madeira_left_0': pygame.transform.scale(pygame.image.load(os.path.join('src','assets', 'images', 'madeira_left_0.png')),(100, 200)),
            'madeira_left_rotate' : pygame.transform.scale(pygame.image.load(os.path.join('src','assets', 'images', 'madeira_left_0_rotate.png')),(200, 100)),
            'madeira_right_100': pygame.transform.scale(pygame.image.load(os.path.join('src','assets', 'images', 'madeira_right_100.png')),(100, 200)),
            'madeira_right_66': pygame.transform.scale(pygame.image.load(os.path.join('src','assets', 'images', 'madeira_right_66.png')),(100, 200)),
            'madeira_right_33': pygame.transform.scale(pygame.image.load(os.path.join('src','assets', 'images', 'madeira_right_33.png')),(100, 200)),
            'madeira_right_0': pygame.transform.scale(pygame.image.load(os.path.join('src','assets', 'images', 'madeira_right_0.png')),(100, 200)),
            'madeira_right_rotate' : pygame.transform.scale(pygame.image.load(os.path.join('src','assets', 'images', 'madeira_right_0_rotate.png')),(200, 100)),
            'ninja-main': pygame.transform.scale(pygame.image.load(os.path.join('src','assets', 'images', 'ninja-main.png')),(67,100)),
            'shuriken-ninja': pygame.image.load(os.path.join('src','assets', 'images', 'shuriken-ninja.png')),
            'shuriken': pygame.transform.scale(pygame.image.load(os.path.join('src','assets', 'images', 'shuriken.png')),(30,30)),
            'slice_sound': pygame.mixer.Sound(os.path.join('src','assets', 'sounds', 'slice.wav')),
            'space_ninja_cat': pygame.transform.scale(pygame.image.load(os.path.join('src','assets', 'images', 'space_ninja_cat.png')),(100,100)),
            # 'spikeball': pygame.image.load(os.path.join('src','assets', 'images', 'spikeball.png'))
            'The Rain Formerly Known as Purple': pygame.mixer.music.load(os.path.join('src','assets', 'music', 'The_Rain_Formerly_Known_as_Purple.mp3')),
        }
        pygame.mixer.music.stop()
        self.roda_musica()
        self.state = {}

        self.state.update(updates) #Atualiza o dicionário de estados com as informações passadas da tela anterior (chooseWeapon)    
        if self.state['weapon'] == 'katana':
            self.posicao_inicial = np.array((237, 487))
        elif self.state['weapon'] == 'kunai':
            self.posicao_inicial = np.array((237, 535))
        elif self.state['weapon'] == 'shuriken':
            self.posicao_inicial = np.array((237, 550))
        self.ball = Ball.Ball(self.state['weapon'],self.level,self.posicao_inicial, [1220,650])
        self.madeiras_sprite = self.cria_sprites_e_madeiras()
        self.enemy = Enemy.Enemy(1, 1100, 500)
        self.planeta = Planet.Planet.change_level(self.level, self.assets['space_ninja_cat'])

    def cria_sprites_e_madeiras(self):
        madeiras_sprite = pygame.sprite.Group()
        madeiras = Madeira.MadeiraSprite.change_level(self.level)
        for madeira in madeiras:
            madeiras_sprite.add(madeira)
        return madeiras_sprite
    
    def atualiza_sprites_e_madeiras(self, madeiras_sprite):
        for madeira in madeiras_sprite:
            if not madeira.morta:
                if self.colisao_quadrados(self.ball.posicao[0], self.ball.posicao[1],self.ball.width, self.ball.height, madeira.x+30, madeira.y, 70, 200):
                    self.assets['chop_wood'].set_volume(0.3)
                    self.assets['chop_wood'].play()
                    madeira.set_life(madeira.vida - self.ball.damage)
                    if madeira.vida <= 0:
                        madeira.morta = True
                    else:
                        self.ball.posicao = self.posicao_inicial
                        self.ball.ammo -= 1
                        self.ball.reset_ball()
                
    def checa_saiu_tela(self):
        if self.ball.posicao[0] < 0 or self.ball.posicao[0] > 1280 or self.ball.posicao[1] < 0 or self.ball.posicao[1] > 720:
            self.ball.reset_ball()
            self.ball.ammo -= 1
            self.ball.posicao = self.posicao_inicial
            
    def atualiza_inimigo_e_confere_vitoria(self):
        self.enemy.render(self.window, self.assets, self.enemy.x, self.enemy.y)
        if self.colisao_quadrados(self.ball.posicao[0], self.ball.posicao[1],self.ball.width, self.ball.height, self.enemy.x, self.enemy.y, 100, 100):
            self.assets['cut_enemy_sound'].set_volume(0.25)
            self.assets['cut_enemy_sound'].play()
            self.enemy.health -= self.ball.damage
            self.ball.reset_ball()
            self.ball.posicao = self.posicao_inicial
            self.ball.ammo -= 1
            if self.enemy.health <= 0:
                self.level += 1
                if self.level == 4:
                    self.victory = True
                    self.level = 3
                self.enemy.change_level(self.level)
                self.madeiras_sprite = self.cria_sprites_e_madeiras(2)
                self.ball.posicao = self.posicao_inicial
                self.ball.reset_ball()
                self.ball.change_type(self.state['weapon'], self.level)

    def desenha(self,display): 
        self.window = display
        self.window.fill((0, 0, 0))
        self.window.blit(self.assets['fundo'], (0, 0))
            
        self.window.blit(self.assets['ninja-main'], (180, 500))
        if not self.ball.get_status():
            if self.state['weapon'] == 'katana':
                self.window.blit(self.assets['katana'], (237, 487))
            elif self.state['weapon'] == 'kunai':
                self.window.blit(self.assets['kunai'], (237, 535))
            elif self.state['weapon'] == 'shuriken':
                self.window.blit(self.assets['shuriken'], (237, 550))

        #planetas
        self.planeta.draw(self.window)

        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("Shots left: " + str(self.ball.ammo), True, (255, 255, 255))
        self.window.blit(text, (1000, 50))
        
        for sprite in self.madeiras_sprite:
            sprite.render(self.window, self.assets)
        self.ball.desenha(self.window, self.assets)
        self.atualiza_sprites_e_madeiras(self.madeiras_sprite)
        self.checa_saiu_tela()
        self.atualiza_inimigo_e_confere_vitoria()
        
        self.ball.aceleracao, self.ball.velocidade = self.planeta.calcula_gravidade(self.ball.posicao, self.ball.aceleracao, self.ball.velocidade, self.ball.height, self.ball.width, self.window)
        if self.planeta.colisao_bola(self.ball.posicao):
            self.ball.aceleracao = self.ball.aceleracao + 0.0001
            
        pygame.display.update()
        
    def distancia(self, x1, y1, x2, y2):
        return math.sqrt((x1-x2)**2 + (y1-y2)**2)
    
    def roda_musica(self):
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)

    def colisao_quadrados(self, x1, y1, w1, h1, x2, y2, w2, h2):
        pygame.Rect(x1, y1, w1, h1)
        pygame.Rect(x2, y2, w2, h2)
        return pygame.Rect.colliderect(pygame.Rect(x1, y1, w1, h1), pygame.Rect(x2, y2, w2, h2))
    
    def atualiza_estado(self):
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                return False
            elif ev.type == pygame.MOUSEBUTTONDOWN:
                if self.ball.verifica_ammo():
                    if self.ball.get_status() == 'NÃO LANÇADA':
                        self.assets['slice_sound'].set_volume(0.15)
                        self.assets['slice_sound'].play()
                        self.ball.lancamento(pygame.mouse.get_pos())
        # Atualiza a posição da bola
        if self.ball.existe:
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
