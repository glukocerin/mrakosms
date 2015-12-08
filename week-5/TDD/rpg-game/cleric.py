from character import Character

class Cleric(Character):
    def heal(self, friend):
        friend.hp += 10
