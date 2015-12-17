import monster
import player
import character
import menu_item

class Game:
    def __init__(self):
        pass

    def start(self):
        monster.monster.new_monster()
        print(player.user.get_username())
        print(monster.monster.get_stats('Dexterity'))
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
        var_player = player.user.stats['Dexterity'] + self.roll(2)
        var_monster = monster.monster.stats['Dexterity'] + self.roll(2)
        if var_player >+ var_monster:
            print('You hit the monster')
        print('You hit the monster')
        return menu_item.strike_menu.display()

    def roll(self, piece):
        return character.Character.dice(self, 2) + 6




game = Game()


