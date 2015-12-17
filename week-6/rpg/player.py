from character import Character
import menu_item
import message as mg
import time
import json
import os

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
        wait(2)
        print()
        for item in self.stats:
            wait(2)
            print(item, ': ', self.stats[item], sep='')
        wait(2)
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

    def create_dict(self):
        return {'name': self.name,
                'stats': self.stats,
                'start stats': self.start_stats,
                'inventory': self.inventory
                }

    def add_item(self):
        filename = input('Please enter a filename: ')
        self.dict = self.create_dict()
        self.save(filename, self.dict)

    def save(self, name, item):
        filename = open('datas/' + name + '.json', 'w')
        json.dump(item, filename)
        filename.close()

    def list_files(self):
        files = []
        for file in os.listdir('datas'):
            if file.endswith(".json"):
                files.append(file)
        for item in files:
            print(item.split('.')[0])

    def load(self, saved_file):
        loaded_files = []
        filename = open('datas/' + saved_file + '.json', 'r')
        try:
            loaded_files = json.load(filename)
        except Exception:
            pass
        filename.close()
        self.dict_to_player(loaded_files)

    def dict_to_player(self, saved_dict):
        self.name = saved_dict['name']
        self.stats = saved_dict['stats']
        self.start_stats = saved_dict['start stats']
        self.inventory = saved_dict['inventory']

def wait(num):
    for i in range(num*2):
        time.sleep(0.1)


user = Player()
