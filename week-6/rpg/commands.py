import sys
import os
import menu_item
import message as mg
import time

def load_game():
    print('Indulhat a jatek')

def exit_game():
    if input(mg.exit.ret())== 'y':
        os.system('clear')
        sys.exit()

def quit_menu():
    mg.quit_question.show()
    menu_item.quit_menu.display()

def wait(num):
    for i in range(num*2):
        time.sleep(0.1)

def continue_to_potion():
    mg.choose_potion.show()
    menu_item.potion_menu.display()

def save():
    print('save')

def save_and_quit():
    print('save')

def quit_wo_save():
    os.system('clear')
    sys.exit()

def clear():
    os.system('clear')

def start():
    print('Elindult a jatek')



