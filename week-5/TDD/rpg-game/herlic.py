from character import Character

class Herlic(Character):
    def heal(self, friend):
        friend.hp += 10
