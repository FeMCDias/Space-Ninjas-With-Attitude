class Madeira:
    def __init__(self, type, x, y, vida=100):
        self.type = type
        self.x = x
        self.y = y
        self.vida = vida
        self.image = None
        
        if type == 'left':
            self.image = 'madeira_left_100.png'
        elif type == 'right':
            self.image = 'madeira_right_100.png'

    def set_image(self, life, type):
        if type == 'left':
            if life == 100:
                self.image = 'madeira_left_100.png'
            elif life == 66:
                self.image = 'madeira_left_66.png'
            elif life == 33:
                self.image = 'madeira_left_33.png'
        elif type == 'right':
            if life == 100:
                self.image = 'madeira_right_100.png'
            elif life == 66:
                self.image = 'madeira_right_66.png'
            elif life == 33:
                self.image = 'madeira_right_33.png'

    def set_life(self, life):
        self.vida = life
        self.set_image(life, self.type)
