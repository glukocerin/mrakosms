class Player:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.max_hp = 10000


    def print_status(self):
        if self.hp <= 0:
            print(self.name, ' is dead.')
        elif self.hp == self.max_hp:
            print(self.name + ' has maximum hp: ' + str(self.hp))
        else:
            print(self.name + '\'s current hp: ' + str(self.hp))

    def drink_potion(self):
        self.hp += 10

    def strike(self, enemy):
        enemy.hp -= self.damage
        print('Enemy HP' + str(enemy.hp))

    def status(self):
        print('Name: ' + self.name)
        print('HP: ' + str(self.hp))
        print('Damage: ' + str(self.damage))

class Cerlic(Player):
    def heal(self, ally):
        ally.hp += 10
        print('Ally HP: ' + str(ally.hp))



balrog = Player('Balrog', 100, 20)
gandalf = Player('Gandalf', 50, 40)
melkor = Cerlic('Melkor', 1000, 80)

balrog.print_status()
for i in range(3):
    gandalf.strike(balrog)
    melkor.heal(balrog)
balrog.print_status()
