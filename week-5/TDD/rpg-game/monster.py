from character import Character

class Monster(Character):
    def strike(self, enemy):
        self.hp += 2
        super().strike(enemy)
