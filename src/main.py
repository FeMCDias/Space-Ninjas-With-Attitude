import pygame
import numpy as np
import math

def inicializa():
    pygame.init()
    pygame.mixer.init()
    window = pygame.display.set_mode((1244, 700), vsync=True, flags=pygame.SCALED)
    pygame.key.set_repeat(50)
    BLACK = (0, 0, 0)
    clock = pygame.time.Clock()
    FPS = 60  # Frames per Second

#----Inicializa as telas

#---- Guarda todos os assets(Músicas, Imagens, Fontes, Telas) em um dicionario. 
    assets = {

#---- Guarda valores que mudam conforme o andar do jogo, dicionário com chaves
#       e valores como: mouse_pressed, tela atual, se o jogo está rodando, etc.
    }
    state = {
        'quitou': False,
    }
    return window, assets, state


# apenas para a formações das telas de menu, regras e morte
def desenha_tela(window: pygame.Surface, state):
    window.fill((0, 0, 0))

def desenha(window: pygame.Surface, assets, state):
    window.blit(assets['background'], (0,0))
    pygame.display.update()
    
def calcula_vetor(state):
    pass

def roda_musica(porcentagem, assets, state):
    state['relogio_musica'].tick()
    pygame.mixer.music.stop()
    pygame.mixer.music.unload()
    pygame.mixer.music.load(assets['NOME DA MÚSICA'])
    pygame.mixer.music.set_volume(0.9)
    pygame.mixer.music.play()
    state['nome_musica_tocando'] = 'NOME DA MÚSICA'

def colisao_ponto_circulo(ponto_x, ponto_y, circulo_x, circulo_y, circulo_raio):
    if math.sqrt((ponto_x-circulo_x)**2 + (ponto_y-circulo_y)**2) <= circulo_raio:
        return True
    return False

def atualiza_estado(assets, state):
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            return False
        elif ev.type == pygame.MOUSEBUTTONDOWN:
            if ev.button == 1:
                state['mouse_pressed'] = True
        elif ev.type == pygame.MOUSEBUTTONUP:
            if ev.button == 1:
                state['mouse_pressed'] = False 
   # Keep Track of Time Here
    return True


# gameloop principal
def gameloop(window, assets, state):
    while atualiza_estado(assets,state):
        desenha_tela(window,state)
        pygame.display.update()


# reseta as funcionalidades do jogo enquanto você reinicia ele (apertar o botão de jogar novamente na tela de morte)
def reset_gameloop(state, assets):
    pass

# finaliza o jogo
def finaliza():
    pygame.quit()

# começa a rodar o programa
if __name__ == '__main__':
    window, assets, state = inicializa()
    gameloop(window, assets, state)
    finaliza()