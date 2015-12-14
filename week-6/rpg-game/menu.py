def print_menu():
    print('(N)ew Game, (L)oad Game, (E)xit')
    print(main_menu(input('Choose an item: ')))


def main_menu(inputstr):
    while inputstr.upper() != 'E':
        if inputstr.upper() == 'N':
            return print_sub_menu_new_game()
        elif inputstr.upper() == 'L':
            return print_sub_menu_load_game()
        print('No option choose from the list')
        print_menu()

def print_sub_menu_new_game():
    print('New game submenu items')


def print_sub_menu_load_game():
    print('Load game submenu items')


def sub_menu_new_game(inputstr):
    pass

def sub_menu_load_game(inputstr):
    pass

