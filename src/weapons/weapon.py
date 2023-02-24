# class weapon with 3 subclasses: shuriken, katana, and kunai. the nature of the object is defined in the constructor, a string with the name of the weapon
class Weapon:
    def __init__(self, name, level):
        self.name = name
        if name == 'shuriken':
            self.weight = 0.5
            self.damage = 40
            self.image = 'shuriken.png'
            self.ammo = 7 + level * 2
        elif name == 'katana':
            self.weight = 3
            self.damage = 75
            self.image = 'katana.png'
            self.ammo = 3 + level * 2
        elif name == 'kunai':
            self.weight = 0.75
            self.damage = 57.5
            self.image = 'kunai.png'
            self.ammo = 5 + level * 2
        else:
            raise Exception('Invalid weapon name')
        
    def change_type(self, name, level):
        self.name = name
        if name == 'shuriken':
            self.weight = 0.5
            self.damage = 40
            self.image = 'shuriken.png'
            self.ammo = 7 + level * 2
        elif name == 'katana':
            self.weight = 3
            self.damage = 75
            self.image = 'katana.png'
            self.ammo = 3 + level * 2
        elif name == 'kunai':
            self.weight = 0.75
            self.damage = 57.5
            self.image = 'kunai.png'
            self.ammo = 5 + level * 2
        else:
            raise Exception('Invalid weapon name')

