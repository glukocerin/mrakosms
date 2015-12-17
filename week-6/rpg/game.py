import monster
import player
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
        pass




game = Game()


