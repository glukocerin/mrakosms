class Menu:
    def __init__(self, items):
        self.items = items

    def menu_print(self):
        print(self.get_menu())

    def display(self):
        while True:
            self.menu_print()
            choice = input("Choose a number: ").upper()
            self.choose_item(choice)
            if choice == 'Q':
                break

    def get_menu(self):
        return '\n'.join(str(item) for item in self.items)

    def choose_item(self, choice):
        for item in self.items:
            if item.num == choice:
                return item.command()

        return 'Wrong Input'

class MenuItem:
    def __init__(self, num, description, command):
        self.num = num
        self.description = description
        self.command = command

    def __repr__(self):
        return '{} {}'.format(self.num, self.description)


