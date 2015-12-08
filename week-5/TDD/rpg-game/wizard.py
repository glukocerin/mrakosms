from character import Character

class Wizard(Character):
    def __init__(self, name, hp, damage, manna):
        self.manna = manna
        super().__init__(name, hp, damage)

    def strike(self, enemy):
        if self.manna >= 5:
            enemy.hp -= 3 * self.damage
            self.manna -= 5
        else:
            enemy.hp -= self.damage / 3
