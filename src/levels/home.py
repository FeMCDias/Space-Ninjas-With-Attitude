import pygame
import interface

class Home:
    def __init__(self, display, assets, state):
        self.display = display
        self.assets = assets
        self.state = state
        self.buttons = []
        self.buttons.append(interface.Button(100, 100, 200, 100, None, (255, 0, 0), None, (0, 0, 0)))
        self.buttons[0].add_text('Start')
        self.buttons.append(interface.Button(100, 300, 200, 100, None, (255, 0, 0), None, (0, 0, 0)))
        self.buttons[1].add_text('Quit')

    def desenha(self, display, assets, state):
        self.display = display
        self.assets = assets
        self.state = state
        self.display.blit(self.assets['background'], (0, 0))
        for button in self.buttons:
            button.draw(self.display)
        pygame.display.update()

    def atualiza_estado(self, assets, state):
        self.assets = assets
        self.state = state
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                return False
            elif ev.type == pygame.MOUSEBUTTONDOWN:
                if ev.button == 1:
                    state['mouse_pressed'] = True
            elif ev.type == pygame.MOUSEBUTTONUP:
                if ev.button == 1:
                    state['mouse_pressed'] = False
            elif ev.type == pygame.MOUSEMOTION:
                state['mouse_pos'] = ev.pos
        return True
    
    def atualiza(self, assets, state):
        self.assets = assets
        self.state = state
        for button in self.buttons:
            if button.is_clicked(self.state['mouse_pos']):
                if self.state['mouse_pressed']:
                    if button.text == 'Start':
                        self.state['level'] = 'level1'
                    elif button.text == 'Quit':
                        return False
        return True
    
    def run(self):
        while self.atualiza_estado(self.assets, self.state):
            self.atualiza(self.assets, self.state)
            self.desenha(self.display, self.assets, self.state)
            if self.state['level'] != 'home':
                return self.state['level']
            
        return False

