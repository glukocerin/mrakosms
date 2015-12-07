from character import Character

class Monster(Character):
    def strike(self, enemy):
        enemy.hp -= self.damage
        self.hp += 2
