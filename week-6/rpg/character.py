import random
import message as mg
import copy

class Character:
    def __init__(self):
        self.name = ''
        self.stats = {'Dexterity': 0, 'Health': 0, 'Luck': 0}
        self.start_stats = {'Dexterity': 0, 'Health': 0, 'Luck': 0}
        self.inventory = {'Selected potion': None, 'Sword': 1, 'Armor': 1}

    def get_username(self):
        return self.name

    def set_username(self):
        self.name = input(mg.set_name.ret())
        print(mg.name_is_correct.ret(), self.name)

    def set_stats(self):
        for item in self.stats:
            if item == 'health':
                self.stats[item] = self.dice(2) + 12
            self.stats[item] = self.dice(1) + 6

    def set_start_stats(self):
        self.start_stats = copy.deepcopy(self.stats)

    def get_stats(self, item):
        return item + ': ' + str(self.stats[item])

    def get_start_stats(self, item):
        return item + ': ' + str(self.start_stats[item])

    def get_inventory(self, item):
        return item + ': ' + str(self.inventory[item])

    def dice(self, piece):
        result = 0
        for n in range(piece):
            result += random.randint(1,6)
        return result
