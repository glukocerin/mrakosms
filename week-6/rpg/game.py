import monster
import player
import character
import menu_item
import random
import copy

class Game:
    def __init__(self):
        pass

    def start(self):
        monster.monster.new_monster()
        monster.monster.set_stats()
        return self.refight()


    def refight(self):
        print(player.user.get_username())
        print(player.user.get_stats('Dexterity'))
        print(player.user.get_stats('Health'), '- max', player.user.get_start_stats('Health'))
        print(monster.monster.get_stats('Luck'))
        print(player.user.get_inventory('Selected potion'))
        print(player.user.get_inventory('Sword'))
        print(player.user.get_inventory('Armor'))
        print()
        print('Monster stats:')
        print('Name:', monster.monster.name)
        print(monster.monster.get_stats('Health'))
        print(monster.monster.get_stats('Dexterity'))
        print()
        return menu_item.figth_menu.display()

    def strike(self):
        print()
        self.var_player = player.user.stats['Dexterity'] + self.roll(2)
        self.var_monster = monster.monster.stats['Dexterity'] + self.roll(2)
        if self.var_player >= self.var_monster:
            print('You hit the monster')
        else:
            print('Monster hit you')
        return menu_item.strike_menu.display()

    def continue_fight(self):
        if self.var_player >= self.var_monster:
            monster.monster.stats['Health'] -= 2
        else:
            player.user.stats['Health'] -= 2
        return self.refight()

    def try_luck(self):
        var = self.roll(2)
        if self.var_player < self.var_monster:
            if var < player.user.stats['Luck']:
                print('health -3')
                player.user.stats['Health'] -= 3
            else:
                print('health -1, luck -1')
                player.user.stats['Health'] -= 1
                player.user.stats['Luck'] -= 1
        else:
            if var < player.user.stats['Luck']:
                print('health -1')
                player.user.stats['Health'] -= 1
            else:
                print('healt - 4, luck -1')
                player.user.stats['Health'] -= 4
                player.user.stats['Luck'] -= 1
        return self.refight()


    def roll(self, piece):
        return self.dice(piece) + 6

    def dice(self, piece):
        result = 0
        for n in range(piece):
            result += random.randint(1,6)
        return result


game = Game()


