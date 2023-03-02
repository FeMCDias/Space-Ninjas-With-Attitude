import pygame

# Classe que instancia um inimigo, com um nível, posição, vida e cor
# De acordo com o nível, o inimigo tem uma vida e cor diferentes
class Enemy:
    def __init__(self, level):
        self.level = level
        if level == 1:
            self.x, self.y = 1100, 500
            self.health = 100
            self.total_health = 100
            self.color = (0, 0, 255)
            self.image = 'enemy1'
        elif level == 2:
            self.x, self.y = 1100, 200
            self.health = 200
            self.total_health = 200
            self.color = (0, 255, 0)
            self.image = 'enemy2'
        elif level == 3:
            self.x, self.y = 1100, 350
            self.health = 300
            self.total_health = 300
            self.color = (255, 0, 0)
            self.image = 'enemy3'
        else:
            raise Exception('Invalid enemy level')
    
    # Função que renderiza o inimigo na tela, com a vida e cor correspondentes
    def change_level(self, level):
        self.level = level
        if level == 1:
            self.x, self.y = 1100, 500
            self.health = 100
            self.total_health = 100
            self.color = (0, 0, 255)
            self.image = 'enemy1'
        elif level == 2:
            self.x, self.y = 1100, 200
            self.health = 200
            self.total_health = 200
            self.color = (0, 255, 0)
            self.image = 'enemy2'
        elif level == 3:
            self.x, self.y = 1100, 350
            self.health = 300
            self.total_health = 300
            self.color = (255, 0, 0)
            self.image = 'enemy3'
        else:
            raise Exception('Invalid enemy level')

    # Função que renderiza o inimigo na tela, com a vida e cor correspondentes
    def render(self, window, assets, x, y):
        window.blit(assets[self.image], (x, y))
        pygame.draw.rect(window, (255, 0, 0), (x, y-10, 100, 10))
        pygame.draw.rect(window, (0, 255, 0), (x, y-10, self.health/self.total_health*100, 10))
        pygame.draw.rect(window, (0, 0, 0), (x, y-10, 100, 10), 1)
        # tiny rect around health_text
        health_text = pygame.font.SysFont('Bauhaus 93', 20).render(str(self.health), True, (0, 0, 0))
        pygame.draw.rect(window, (255, 255, 255), (x+50-health_text.get_width()/2, y-15-health_text.get_height()/2, health_text.get_width(), health_text.get_height()))
        window.blit(health_text, (x+50-health_text.get_width()/2, y-15-health_text.get_height()/2))