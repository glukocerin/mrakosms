class Warrior:
    def __init__(self):
        self.companions = []
        self.hp = 100

    def join(self, companion):
        self.companions.append(companion)

    def strike(self, opponent):
        opponent.infilct_damage(10)

    def infilct_damage(self, damage):
        self.hp -= damage
        for companion in self.companions:
            companion.notify('damage', self)

class Field:
    
    def notify(self, type, warrior):
        if type == 'damage':
            print('van egy halottunk')


warrior = Warrior()
warrior2 = Warrior()
field = Field()

warrior.join(field)
warrior2.join(field)
warrior.strike(warrior2)
