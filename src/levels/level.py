import pygame
import pymunk as pm
import math
import interface
class level:
    def __init__(self) -> None:
        pygame.init()
        pygame.mixer.init()
        self.window = pygame.display.set_mode((1244, 700), vsync=True, flags=pygame.SCALED)
        pygame.key.set_repeat(50)
        self.BLACK = (0, 0, 0)
        self.clock = pygame.time.Clock()
        self.FPS = 60  # Frames per Second
        self.space = pm.Space()
        self.space.gravity = (0.0, -900.0)
        self.assets = {
            'catapulta': pygame.image.load('../assets/images/catapulta.png'),
            'shuriken': pygame.image.load('../assets/images/shuriken.png'),
            'kunai': pygame.image.load('../assets/images/kunai.png'),
            'katana': pygame.image.load('../assets/images/katana.png'),
        }
        self.state = {
            'atirando': False,
            'atirou': False,
            'quitou': False,
        }

    def inicializa(self):
        return self.window, self.assets, self.state
    
    # apenas para a formações das telas de menu, regras e morte
    def desenha_tela(self, window: pygame.Surface, state):
        window.fill((0, 0, 0))

    def desenha(self, window: pygame.Surface, assets, state): 
        if state['weapon'] == 'katana':
            window.blit(pygame.transform.scale(assets['katana'], (50, 100)), (180, 500))
        elif state['weapon'] == 'kunai':
            window.blit(pygame.transform.scale(assets['kunai'], (50, 100)), (180, 500))
        elif state['weapon'] == 'shuriken':
            window.blit(pygame.transform.scale(assets['shuriken'], (50, 50)), (180, 500))

        window.blit(pygame.transform.scale(assets['catapulta'], (50, 100)), (180, 500))
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
    
    def atualiza_estado(self, assets, state):
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                return False
            elif ev.type == pygame.MOUSEBUTTONDOWN:
                if self.colisao_ponto_circulo(ev.pos[0], ev.pos[1], 180, 500, 50) and not state['atirou']: 
                    state['atirando'] = True
            elif ev.type == pygame.MOUSEBUTTONUP:
                if state['atirando']:
                    state['atirando'] = False
                    state['atirou'] = True
            if state['atirando']:
                state['vetor'] = self.vector((180, 500), ev.pos)
                print(state['atirando'], state['atirou'])
            if state['atirou']:
                state['atirou'] = False
                print(state['vetor'])
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

        
   
