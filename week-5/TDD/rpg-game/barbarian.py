from character import Character

class Barbarian(Character):
    def strike(self, enemy):
        enemy.hp -= 2 * self.damage
