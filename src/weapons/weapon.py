# A classe "Weapon" define uma arma com atributos como nome, peso, dano e munição. 
# Possui um construtor que recebe nome e nível, um método para trocar o tipo de arma e
# três métodos para retornar a quantidade de munição, dano e nome da arma. 
class Weapon:
    # Ao instanciar a classe, o construtor recebe o nome da arma e o nível do jogador
    # e define os atributos da arma de acordo com o nome e nível
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
        
    # Método para trocar o tipo de arma
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

    # Métodos para retornar a quantidade de munição, dano e nome da arma 
    def get_ammo(self):
        return self.ammo
    
    def get_damage(self):
        return self.damage
    
    def get_name(self):
        return self.name
        

