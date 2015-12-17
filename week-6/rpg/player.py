from character import Character
import menu_item
import commands as cmd
import message as mg

class Player(Character):
    def new_player(self):
        self.set_username()
        return menu_item.new_game.display()

    def roll_stats(self):
        self.set_stats()
        self.set_start_stats()
        return self.start_roll_display()

    def start_roll_display(self):
        mg.start_roll.show()
        cmd.wait(2)
        print()
        for item in self.stats:
            cmd.wait(2)
            print(item, ': ', self.stats[item], sep='')
        cmd.wait(2)
        print()
        return menu_item.roll_menu.display()

    def set_potion(self, arg):
        self.inventory['Selected potion'] = arg
        self.get_potion()

    def get_potion(self):
        print(mg.set_potion.ret(), self.inventory['Selected potion'])
        return menu_item.potion_submenu.display()

    def get_character_stats(self):
        print(mg.begin_welcome.ret())
        print(mg.your_name.ret(), self.get_username())
        for item in self.stats:
            print(self.get_stats(item))
        mg.inventory.show()
        for item in self.inventory:
            print(self.get_inventory(item))
        print()
        return menu_item.potion_begin_menu.display()



user = Player()
