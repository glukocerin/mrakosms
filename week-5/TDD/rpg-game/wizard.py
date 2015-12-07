from character import Character

class Wizard(Character):
    def __init__(self, name, hp, damage, manna):
        self.manna = manna
        super().__init__(name, hp, damage)

    def strike(self, enemy):
        enemy.hp -= self.damage
        self.manna -= 5
