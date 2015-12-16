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
                if choice > len(self.items):
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
# class NewGame(Menu):
#     pass

# class LoadGame(Menu):
#     pass


class MenuItem:
    def __init__(self, num, description, command, arg = None):
        self.num = num
        self.description = description
        self.command = command
        self.arg = arg

    def __repr__(self):
        return '{} {}'.format(self.num, self.description)


