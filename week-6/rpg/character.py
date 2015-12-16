import random
# import commands as cmd

class Character:
    def __init__(self):
        self.name = ''
        self.dexterity = 0
        self.health = 0
        self.luck = 0
        self.start_stats = {'dexterity': 0, 'health': 0, 'luck': 0}
        self.inventory = {'Selected potion': None, 'Sword': 1, 'Armor': 1}

    def get_username(self):
        return self.name

    def set_username(self):
        self.name = input('nev: ')

    def set_stats(self):
        self.set_dexterity()
        self.set_healt()
        self.set_luck()

    def set_start_stats(self):
        self.start_stats['dexterity'] = self.get_dexterity()
        self.start_stats['health'] = self.get_healt()
        self.start_stats['luck'] = self.get_luck()
        # return cmd.new_game()

    def get_stat(self):
        self.get_dexterity()
        self.get_healt()
        self.get_luck()

    def get_start_stats(self, item):
        return item + ': ' + str(self.start_stats[item])

    def get_dexterity(self):
        return self.dexterity

    def set_dexterity(self):
        self.dexterity = self.dice(1) + 6

    def get_healt(self):
        return self.health

    def set_healt(self):
        self.health = self.dice(2) + 12

    def get_luck(self):
        return self.luck

    def set_luck(self):
        self.luck = self.dice(1) + 6

    def dice(self, piece):
        result = 0
        for n in range(piece):
            result += random.randint(1,6)
        return result




