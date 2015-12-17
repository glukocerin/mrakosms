import sys
import os
import menu_item
import message as mg
import player

def no_work():
    print('no work')

def load_game():
    player.user.list_files()
    print()
    player.user.load(input('Enter the filename: '))
    player.user.get_character_stats()

def exit_game():
    if input(mg.exit.ret())== 'y':
        os.system('clear')
        sys.exit()

def quit_menu():
    mg.quit_question.show()
    menu_item.quit_menu.display()

def continue_to_potion():
    mg.choose_potion.show()
    menu_item.potion_menu.display()

def save():
    menu_item.save_game.display()

def save_and_quit():
    player.user.add_item()
    os.system('clear')
    sys.exit()

def quit_wo_save():
    os.system('clear')
    sys.exit()

def clear():
    os.system('clear')
