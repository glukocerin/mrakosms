import message
import os

class Menu:
    def __init__(self, items):
        self.items = items

    def display(self):
        while True:
            try:
                self.menu_print()
                choice = int(input(message.choose.ret()))
                if choice > len(self.items) or choice < 1:
                    message.wrong_integer.show()
                else:
                    self.choose_item(choice)
            except Resume:
                break
            except ValueError:
                message.no_integer.show()

    def menu_print(self):
        print(self.get_menu())

    def get_menu(self):
        return '\n'.join(str(item) for item in self.items)

    def choose_item(self, choice):
        for item in self.items:
            if item.num == choice:
                if item.arg == None:
                    return item.command()
                else:
                    return item.command(item.arg)
        return 'Wrong Input'

class Resume(Exception):
    pass

def resume():
    raise Resume

# def start(self, next):
#         while True:
#             next = self.menu[next]()
#             if next == 'exit':
#                 break

# def new_game():
#     item = [
#                 ('1', {'title': 'reenter name', 'id':'newre'}),
#                 ('2', {'title': 'Continue', 'id':'new'}),
#                 ('3', {'title': 'Save', 'id' : 'new'}),
#                 ('4', {'title': 'Quit', 'id': 'quit' })
#     ]
#     print('\n'+'\n'.join([x[0] + ' ' + x[1]['title'] for x in l])+'\n')
#     menu = {x[0]: x[1] for x in l}
#     choosen_menu_id = input('Choose from the menu: ')
#     return start[choosen_menu_id]['id']


# new_game = (
#             {'newre', 'player.user.new_player'},
#             {2, 'player.user.roll_stats'},
#             {3, 'cmd.save'},
#             {4, 'cmd.quit_menu'}
# )

# main_menu = [
#     (1, mg.new_game.ret(), player.user.new_player),
#     (2, mg.load_game.ret(), cmd.load_game),
#     (3, mg.exit_game.ret(), cmd.exit_game)
# ]
