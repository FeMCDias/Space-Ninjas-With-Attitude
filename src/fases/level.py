import pygame
import pymunk as pm
import math
import interface
import os
import numpy as np

class level:
    def __init__(self) -> None:
        pygame.init()
        pygame.mixer.init()
        self.window = pygame.display.set_mode((1220, 650), vsync=True, flags=pygame.SCALED)
        pygame.key.set_repeat(50)
        self.BLACK = (0, 0, 0)
        self.clock = pygame.time.Clock()
        self.FPS = 60  # Frames per Second
        self.space = pm.Space()
        self.space.gravity = (0.0, -900.0)
        
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
            'spikeball': pygame.image.load(os.path.join('src','assets', 'images', 'spikeball.png')),
            # add all images from assets here

        }
        self.state = {
            'atirando': False,
            'atirou': False,
            'quitou': False,
            'bola':{
                'center': (0, 0),
            }
        }

        #lançamento da arma
        self.pos_mouse = np.array([0, 0])
        

    def inicializa(self):
        return self.window, self.assets, self.state
    
    # apenas para a formações das telas de menu, regras e morte
    def desenha_tela(self, window: pygame.Surface, state):
        window.fill((0, 0, 0))
        self.window.blit(self.assets['fundo'], (0, 0))

    def desenha(self, window: pygame.Surface, assets, state): 
        window.blit(pygame.transform.scale(assets['ninja-main'], (67, 100)), (180, 500))
        if state['weapon'] == 'katana':
            window.blit(pygame.transform.scale(assets['katana'], (50, 80)), (237, 487))
        elif state['weapon'] == 'kunai':
            window.blit(pygame.transform.scale(assets['kunai'], (50, 100)), (237, 510))
        elif state['weapon'] == 'shuriken':
            window.blit(pygame.transform.scale(assets['shuriken'], (25, 25)), (237, 550))
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
    
    def desenha_flecha(self, window, ponto, direcao, alcance):
    #desenhar a flecha de acordo com a formula da trajetória de um projétil
        pygame.draw.line(window, (255, 255, 255), ponto, (ponto[0] + alcance*math.cos(direcao), ponto[1] + alcance*math.sin(direcao)), 3)
        pygame.display.update()


    def desenha_bola(self, window, x, y):
        # apenas desenha a bola pygame
        bola = pygame.draw.circle(window, (255, 255, 255), (x, y), 10)
        pygame.display.update()
        return bola
    
    def reblit(self, window, state):
        self.window.fill((0, 0, 0))
        self.window.blit(self.assets['fundo'], (0, 0))
        self.window.blit(pygame.transform.scale(self.assets['ninja-main'], (67, 100)), (180, 500))
        if state['weapon'] == 'katana':
            self.window.blit(pygame.transform.scale(self.assets['katana'], (50, 80)), (237, 487))
        elif state['weapon'] == 'kunai':
            self.window.blit(pygame.transform.scale(self.assets['kunai'], (50, 100)), (237, 510))
        elif state['weapon'] == 'shuriken':
            self.window.blit(pygame.transform.scale(self.assets['shuriken'], (25, 25)), (237, 550))


    def atualiza_estado(self, assets, state):
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                return False
            elif ev.type == pygame.MOUSEBUTTONDOWN:
                if self.colisao_ponto_circulo(ev.pos[0], ev.pos[1], 230, 550, 70) and not state['atirou']: 
                    state['atirando'] = True
                # enquanto o mouse estiver pressionado, a flecha é desenhada e atualizada a cada frame
                if state['atirando']:
                    if self.distancia(ev.pos[0], ev.pos[1], 230, 550) <= 100:
                        self.desenha_flecha(self.window, (230, 550), math.atan2(ev.pos[1]-550, ev.pos[0]-230), self.distancia(ev.pos[0], ev.pos[1], 230, 550))

            elif ev.type == pygame.MOUSEBUTTONUP:
                pass
                # # se o mouse for solto, a bola é lançada
                # while state['atirando']:
                #     # a bola começa em x=180, y=500
                #     x = 180
                #     y = 500
                #     self.desenha_bola(self.window, x, y)
                #     # até encostar na borda da tela
                #     if x < 0 or x > 600 or y < 0 or y > 600:
                #         state['atirando'] = False
                #         state['atirou'] = True
                #         self.reblit(self.window, state)
                #         break
                
        return True

    def gameloop(self, window, assets, state):
        while self.atualiza_estado(assets,state):
            self.desenha_tela(window,state)
            self.desenha(window, assets, state)
            pygame.display.update()

    def reset_gameloop(self, state, assets):
        pass

    def vector(self, p1, p2):
        """Return the vector from p1 to p2"""
        return (p2[0]-p1[0], p2[1]-p1[1])
    
    def unit_vector(self, v):
        """Return the unit vector of the vector v"""
        norm = math.sqrt(v[0]**2+v[1]**2)
        return (v[0]/norm, v[1]/norm)


    def finaliza(self):
        pygame.quit()

        
   
