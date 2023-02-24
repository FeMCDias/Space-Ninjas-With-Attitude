import pygame
import interface.interface as interface
import levels.level as level

class Home:
    def __init__(self, display):
        self.display = display
        self.buttons = []
        self.buttons.append(interface.Button(100, 100, 200, 100, None, (255, 0, 0), None, (0, 0, 0)))
        self.buttons[0].add_text('Start')
        self.buttons.append(interface.Button(100, 300, 200, 100, None, (255, 0, 0), None, (0, 0, 0)))
        self.buttons[1].add_text('Quit')

    def desenha(self, display):
        self.display = display
        for button in self.buttons:
            button.draw(self.display)
        pygame.display.update()

    def atualiza_estado(self):
  
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                return False
            elif ev.type == pygame.MOUSEBUTTONDOWN:
                if ev.button == 1:
                    self.state['mouse_pressed'] = True
            elif ev.type == pygame.MOUSEBUTTONUP:
                if ev.button == 1:
                    self.state['mouse_pressed'] = False
            elif ev.type == pygame.MOUSEMOTION:
                self.state['mouse_pos'] = ev.pos
        return True
    
    def gameloop(self, display, assets, state):
        self.display = display
        self.assets = assets
        self.state = state
        while self.atualiza_estado(self.assets, self.state):
            self.desenha(self.display, self.assets, self.state)
            for button in self.buttons:
                if button.is_clicked(self.state['mouse_pos']):
                    if button.text == 'Start':
                        nivel = level.Level(self.display, self.assets, self.state)
                        nivel.gameloop()
                        
                    elif button.text == 'Quit':
                        return False
        return True
    
    def finaliza(self):
        pygame.quit()


