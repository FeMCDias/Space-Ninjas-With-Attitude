import pygame
import pymunk as pm
import math
import interface
import os
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
        self.assets = {
            'catapulta': pygame.image.load(os.path.join('assets', 'images', 'catapulta.png')),
            'enemy1': pygame.image.load(os.path.join('assets', 'images', 'enemy1.png')),
            'enemy2': pygame.image.load(os.path.join('assets', 'images', 'enemy2.png')),
            'enemy3': pygame.image.load(os.path.join('assets', 'images', 'enemy3.png')),
            'fundo': pygame.image.load(os.path.join('assets', 'images', 'space-ninja-temple.jpg')),
            'katana-ninja': pygame.image.load(os.path.join('assets', 'images', 'katana-ninja.png')),
            'katana': pygame.image.load(os.path.join('assets', 'images', 'katana.png')),
            'kunai-for-character': pygame.image.load(os.path.join('assets', 'images', 'kunai-for-character.png')),
            'kunai-ninja': pygame.image.load(os.path.join('assets', 'images', 'kunai-ninja.png')),
            'kunai': pygame.image.load(os.path.join('assets', 'images', 'kunai.png')),
            'madeira_left_100': pygame.image.load(os.path.join('assets', 'images', 'madeira_left_100.png')),
            'madeira_left_66': pygame.image.load(os.path.join('assets', 'images', 'madeira_left_66.png')),
            'madeira_left_33': pygame.image.load(os.path.join('assets', 'images', 'madeira_left_33.png')),
            'madeira_left_0': pygame.image.load(os.path.join('assets', 'images', 'madeira_left_0.png')),
            'madeira_right_100': pygame.image.load(os.path.join('assets', 'images', 'madeira_right_100.png')),
            'madeira_right_66': pygame.image.load(os.path.join('assets', 'images', 'madeira_right_66.png')),
            'madeira_right_33': pygame.image.load(os.path.join('assets', 'images', 'madeira_right_33.png')),
            'madeira_right_0': pygame.image.load(os.path.join('assets', 'images', 'madeira_right_0.png')),
            'ninja-main': pygame.image.load(os.path.join('assets', 'images', 'ninja-main.png')),
            'shuriken-ninja': pygame.image.load(os.path.join('assets', 'images', 'shuriken-ninja.png')),
            'shuriken': pygame.image.load(os.path.join('assets', 'images', 'shuriken.png')),
            'spikeball': pygame.image.load(os.path.join('assets', 'images', 'spikeball.png')),
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

    def inicializa(self):
        return self.window, self.assets, self.state
    
    # apenas para a formações das telas de menu, regras e morte
    def desenha_tela(self, window: pygame.Surface, state):
        window.fill((0, 0, 0))
        self.window.blit(self.assets['fundo'], (0, 0))

    def desenha(self, window: pygame.Surface, assets, state): 
        window.blit(pygame.transform.scale(assets['ninja-main'], (50, 100)), (180, 500))
        if state['weapon'] == 'katana':
            window.blit(pygame.transform.scale(assets['katana'], (50, 100)), (220, 480))
        elif state['weapon'] == 'kunai':
            window.blit(pygame.transform.scale(assets['kunai'], (50, 100)), (220, 510))
        elif state['weapon'] == 'shuriken':
            window.blit(pygame.transform.scale(assets['shuriken'], (25, 25)), (220, 550))
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
    
    def desenha_flecha(self, window, ponto, direcao):
    #desenhar a flecha de acordo com a formula da trajetória de um projétil
        pygame.draw.line(window, (255, 255, 255), ponto, (ponto[0] + direcao[0]*100, ponto[1] + direcao[1]*100), 5)
        pygame.display.update()


    def desenha_bola(self, window, assets, state):
        # apenas desenha a bola pygame
        bola = pygame.draw.circle(window, (255, 255, 255), (180, 500), 10)
        pygame.display.update()
        return bola
    
    

    def atualiza_estado(self, assets, state):
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                return False
            elif ev.type == pygame.MOUSEBUTTONDOWN:
                if self.colisao_ponto_circulo(ev.pos[0], ev.pos[1], 180, 500, 50) and not state['atirou']: 
                    state['atirando'] = True
                    while ev.type != pygame.MOUSEBUTTONUP:
                        for ev in pygame.event.get():
                            if ev.type == pygame.MOUSEMOTION:
                                state['vetor'] = self.vector((180, 500), ev.pos)
                                self.direcao = self.vector((180, 500), ev.pos)
                                self.desenha_flecha(self.window, (180, 500), self.direcao)
                                pygame.display.update()
                        
            elif ev.type == pygame.MOUSEBUTTONUP:
                # se o mouse for solto, a bola é lançada
                if state['atirando']:
                    print('soltou')
                    state['atirando'] = False
                    state['atirou'] = True
                    for i in range(0, 100):
                        self.desenha_bola(self.window, assets, state)
                        state['bola']['center'] = (state['bola']['center'][0] + self.direcao[0]*i, state['bola']['center'][1] + self.direcao[1]*i)
                        pygame.display.update()
                        self.window.fill((0, 0, 0))
                        self.clock.tick(60)
                    state['atirou'] = False


                   

                    



                


                
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

        
   
