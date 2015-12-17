from character import Character

class Monster(Character):
    def set_start_stat(self):
        self.stats = {'Dexterity': 0, 'Health': 0}

    def new_monster(self):
        self.name = 'Monster'
        # return menu_item.new_game.display()

monster = Monster()
