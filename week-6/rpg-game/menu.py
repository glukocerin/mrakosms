def print_menu():
    print('(N)ew Game, (L)oad Game, (E)xit')

def main_menu():
    print_menu()
    inputstr = input('Valassz')
    while inputstr.upper() != 'E':
        if inputstr.upper() == 'N':
            return print_sub_menu_new_game()
        elif inputstr.upper() == 'L':
            return print_sub_menu_load_game()
        print_menu()
        inputstr = input('Nem jo ujra')

def print_sub_menu_new_game():
    print(sub_menu_new_game())

def print_sub_menu_load_game():
    print(sub_menu_load_game())

def sub_menu_new_game():
    return 'New game submenu items'

def sub_menu_load_game():
    return 'Load game submenu items'

