import random
# import commands as cmd

class Character:
    def __init__(self):
        self.name = ''
        self.stat = {'dexterity': 0, 'health': 0, 'luck': 0}
        self.start_stat = {'dexterity': 0, 'health': 0, 'luck': 0}
        self.inventory = {'Selected potion': None, 'Sword': 1, 'Armor': 1}

    def get_username(self):
        return self.name

    def set_username(self):
        self.name = input('nev: ')

    def set_stats(self):
        for item in self.stat:
            if item == 'health':
                self.stat[item] = self.dice(2) + 12
            self.stat[item] = self.dice(1) + 6

    def set_start_stats(self):
        self.start_stat = self.stat
        # return cmd.new_game()

    def get_stat(self, item):
        return item + ': ' + str(self.stat[item])

    def get_start_stats(self, item):
        return item + ': ' + str(self.start_stat[item])

    def dice(self, piece):
        result = 0
        for n in range(piece):
            result += random.randint(1,6)
        return result




