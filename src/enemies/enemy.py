class Enemy:
    def __init__(self, level):
        self.level = level
        if level == 1:
            self.health = 100
            self.color = (0, 0, 255)
            self.image = 'enemy1.png'
        elif level == 2:
            self.health = 200
            self.color = (0, 255, 0)
            self.image = 'enemy2.png'
        elif level == 3:
            self.health = 300
            self.color = (255, 0, 0)
            self.image = 'enemy3.png'
        else:
            raise Exception('Invalid enemy level')
        
    def change_level(self, level):
        self.level = level
        if level == 1:
            self.health = 100
            self.color = (0, 0, 255)
            self.image = 'enemy1.png'
        elif level == 2:
            self.health = 200
            self.color = (0, 255, 0)
            self.image = 'enemy2.png'
        elif level == 3:
            self.health = 300
            self.color = (255, 0, 0)
            self.image = 'enemy3.png'
        else:
            raise Exception('Invalid enemy level')