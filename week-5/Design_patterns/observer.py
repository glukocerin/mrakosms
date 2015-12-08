
import random

class Warrior:
    def __init__(self):
        self.companions = []
        self.hp = 100

    def join(self, companion):
        self.companions.append(companion)

    def strike(self, opponent):
        opponent.infilct_damage(10)

    def curse(self, opponent):
        opponent.join(Curse())
        self._notify_all('curse')

    def infilct_damage(self, damage):
        self.hp -= damage
        self._notify_all('damage')

    def heal(self, hp):
        self.hp += hp

    def _notify_all(self, type):
        for companion in self.companions:
            companion.notify(type, self)

    def search_gold(self):
        if random.randint(1, 10) > 5:
            for companion in self.companions:
                companion.notify('find gold', self)
        pass



class Healer():
    def notify(self, type, warrior):
        if type == 'damage':
            warrior.heal(10)
        elif type =='find gold':
            warrior.heal(10)

class Curse:
    def notify(self, type, warrior):
        if type == 'damage':
            warrior.heal(-10)

class Cheer:
    def notify(self, type, warrior):
        if type == 'curse':
            print('Hurray')



rabbit = Warrior()
wolf = Warrior()
shaman = Healer()

rabbit.join(shaman)
wolf.join(Cheer())

wolf.curse(rabbit)
wolf.strike(rabbit)
rabbit.search_gold()


print(rabbit.hp)
