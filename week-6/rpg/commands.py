import sys
import os
import menu_item
import player

def new_game():
    menu_item.new_game.display()

def define_player():
    player.user.name = get_username()
    print('Hello', player.user.name)
    return new_game()

def get_username():
    username = input("Type your nameeee: ")
    return username

def load_game():
    print('Load game')

def exit_game():
    return sys.exit()

def continue_():
    print(player.user.health)

def save():
    print('save')

def quit():
    pass

