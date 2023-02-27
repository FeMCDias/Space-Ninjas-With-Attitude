import pygame
import pymunk as pm
import math
import interface
import os
import numpy as np
import weapons.ball as Ball
import weapons.weapon as Weapon

class level():
    def __init__(self, display, updates) -> None:
        pygame.init()
        pygame.mixer.init()
        self.window = display
        pygame.key.set_repeat(50)
        self.BLACK = (0, 0, 0)
        self.clock = pygame.time.Clock()
        self.FPS = 60  # Frames per Second
        self.space = pm.Space()
        self.space.gravity = (0.0, -900.0)
        self.level = 1
        #Imagens
        self.assets = {
            'catapulta': pygame.image.load(os.path.join('src','assets', 'images', 'catapulta.png')),
            'enemy1': pygame.image.load(os.path.join('src','assets', 'images', 'enemy1.png')),
            'enemy2': pygame.image.load(os.path.join('src','assets', 'images', 'enemy2.png')),
            'enemy3': pygame.image.load(os.path.join('src','assets', 'images', 'enemy3.png')),
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
            'spikeball': pygame.image.load(os.path.join('src','assets', 'images', 'spikeball.png'))
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
        
        self.pos_mouse = np.array([0, 0])
        ball = Ball.Ball(self.state['weapon'],self.level,self.pos_mouse, [1220,650])
        print(ball.get_name())



    def inicializa(self):
        return self.window, self.assets, self.state

    def desenha_tela(self):
        self.window.fill((0, 0, 0))
        self.window.blit(self.assets['fundo'], (0, 0))

    def desenha(self,display): 

        self.display = display
        self.desenha_tela()
        self.window.blit(pygame.transform.scale(self.assets['ninja-main'], (67, 100)), (180, 500))
        if self.state['weapon'] == 'katana':
            self.window.blit(pygame.transform.scale(self.assets['katana'], (50, 80)), (237, 487))
        elif self.state['weapon'] == 'kunai':
            self.window.blit(pygame.transform.scale(self.assets['kunai'], (50, 100)), (237, 510))
        elif self.state['weapon'] == 'shuriken':
            self.window.blit(pygame.transform.scale(self.assets['shuriken'], (25, 25)), (237, 550))
        pygame.display.update()

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

    def colisao_ponto_circulo(self, ponto_x, ponto_y, circulo_x, circulo_y, circulo_raio):
        if math.sqrt((ponto_x-circulo_x)**2 + (ponto_y-circulo_y)**2) <= circulo_raio:
            return True
        return False

    def reblit(self,):
        self.window.fill((0, 0, 0))
        self.window.blit(self.assets['fundo'], (0, 0))
        self.window.blit(pygame.transform.scale(self.assets['ninja-main'], (67, 100)), (180, 500))
        if self.state['weapon'] == 'katana':
            self.window.blit(pygame.transform.scale(self.assets['katana'], (50, 80)), (237, 487))
        elif self.state['weapon'] == 'kunai':
            self.window.blit(pygame.transform.scale(self.assets['kunai'], (50, 100)), (237, 510))
        elif self.state['weapon'] == 'shuriken':
            self.window.blit(pygame.transform.scale(self.assets['shuriken'], (25, 25)), (237, 550))


    def atualiza_estado(self):
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                return False
            elif ev.type == pygame.MOUSEBUTTONDOWN:
                pass
            elif ev.type == pygame.MOUSEBUTTONUP:
                pass
                
        return True

    def gameloop(self):
        while self.atualiza_estado(self.assets,self.state):
            self.desenha_tela(self.window,self.state)
            self.desenha(self.window, self.assets, self.state)
            pygame.display.update()


    def finaliza(self):
        pygame.quit()

        
   
