import sys
import os
import menu_item
import player
import printers
import message
import random
import time

def new_game():
    clear()
    printers.hello()
    menu_item.new_game.display()

def define_player():
    player.user.set_username()
    return new_game()

def load_game():
    print()


def exit_game():
    opt = input(message.exit.ret())
    if opt == 'y':
        sys.exit()

def set_start():
    player.user.dexterity = roll() + 6
    player.user.health = roll() + roll() + 12
    player.user.luck = roll() + 6
    player.user.start_dexterity = player.user.dexterity
    player.user.start_health = player.user.health
    player.user.start_luck = player.user.luck

    clear()
    print()
    print('Szia ' + player.user.name + ', most kisorsoljuk az indulo pontjaid')
    wait(2)
    print('Az indulo ugyesseg pontszamod:',player.user.start_dexterity)
    wait(1)
    print('Az indulo eletero pontszamod:',player.user.start_health)
    wait(1)
    print('Az indulo szerencse pontszamod:',player.user.start_luck)
    wait(1)
    print()
    menu_item.roll_menu.display()

def wait(num):
    for i in range(num*2):
        time.sleep(0.1)

def roll():
    return random.randint(1,6)

def continue_reroll():
    clear()
    print()
    message.choose_potion.show()
    menu_item.potion_menu.display()

def set_potion(arg):
    message.set_potion.show()
    player.user.inventory['potion'] = arg
    print(player.user.inventory['potion'])
    menu_item.potion_submenu.display()

def save():
    print('save')

def quit_menu():
    message.quit.show()
    menu_item.quit_menu.display()

def save_and_quit():
    pass


def quit_wo_save():
    sys.exit()

def clear():
    os.system('clear')

def begin():
    print('Indulhatunk')
    print(player.user.health)
    print(player.user.dexterity)
    print(player.user.luck)
    print(player.user.inventory['potion'])
    print(player.user.inventory['Sword'])
    print(player.user.inventory['Armor'])
    menu_item.potion_begin_menu.display()

def start():
    print('Elindult a jatek')



