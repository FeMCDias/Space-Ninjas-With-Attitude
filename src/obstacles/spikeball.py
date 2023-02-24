class SpikeBall:
    def __init__(self, x, y, speed=0, swing_radius=0, image='spikeball.png'):
        self.x = x
        self.y = y
        self.radius = 20
        self.speed = speed
        self.swing_radius = swing_radius
        self.image = image
    
    def get_location(self):
        return (self.x, self.y)
    
    def collision(self, x, y, radius):
        if (self.x - x) ** 2 + (self.y - y) ** 2 <= (self.radius + radius) ** 2:
            return True
        return False