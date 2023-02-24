import pygame
import pymunk as pm
import math

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
            'catapulta': pygame.image.load('assets/images/catapulta.png'),
            'redbird': pygame.image.load('assets/images/shuriken.png'),
        }
        self.state = {
            'quitou': False,
        }
        self.mouse_distance = 0
        self.rope_length = 90
        self.angle = 0
        self.x_mouse = 0
        self.y_mouse = 0
        self.sling_x, self.sling_y = 135, 450
        self.sling2_x, self.sling2_y = 160, 450

    def inicializa(self):
        return self.window, self.assets, self.state
    
    # apenas para a formações das telas de menu, regras e morte
    def desenha_tela(self, window: pygame.Surface, state):
        window.fill((0, 0, 0))

    def desenha(self, window: pygame.Surface, assets, state): 
        window.blit(pygame.transform.scale(assets['catapulta'], (50, 100)), (150, 400))
        window.blit(pygame.transform.scale(assets['redbird'], (50, 50)), (200, 450))
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
                if ev.button == 1:
                    state['mouse_pressed'] = True
            elif ev.type == pygame.MOUSEBUTTONUP:
                if ev.button == 1:
                    state['mouse_pressed'] = False
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
    
    def sling_action(self):
        v = self.vector((self.sling_x, self.sling_y), (self.x_mouse, self.y_mouse))
        uv = self.unit_vector(v)
        uv1 = uv[0]
        uv2 = uv[1]
        mouse_distance = self.distancia(self.sling_x, self.sling_y, self.x_mouse, self.y_mouse)
        pu = (uv1*self.rope_length+self.sling_x, uv2*self.rope_length+self.sling_y)
        bigger_rope = 102
        x_redbird = self.x_mouse - 20
        y_redbird = self.y_mouse - 20
        if mouse_distance > self.rope_lenght:
            pux, puy = pu
            pux -= 20
            puy -= 20
            pul = pux, puy
            self.window.blit(self.redbird, pul)
            pu2 = (uv1*bigger_rope+self.sling_x, uv2*bigger_rope+self.sling_y)
            pygame.draw.line(self.window, (0, 0, 0), (self.sling2_x, self.sling2_y), pu2, 5)
            self.window.blit(self.redbird, pul)
            pygame.draw.line(self.window, (0, 0, 0), (sling_x, sling_y), pu2, 5)
        else:
            mouse_distance += 10
            pu3 = (uv1*mouse_distance+sling_x, uv2*mouse_distance+sling_y)
            pygame.draw.line(self.window, (0, 0, 0), (sling2_x, sling2_y), pu3, 5)
            self.window.blit(redbird, (x_redbird, y_redbird))
            pygame.draw.line(self.window, (0, 0, 0), (sling_x, sling_y), pu3, 5)
        # Angle of impulse
        dy = self.y_mouse - self.sling_y
        dx = self.x_mouse - self.sling_x
        if dx == 0:
            dx = 0.00000000000001
        angle = math.atan((float(dy))/dx)


    def finaliza(self):
        pygame.quit()

        
   
