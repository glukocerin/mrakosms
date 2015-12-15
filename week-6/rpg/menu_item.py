from menu import Menu, MenuItem
import commands


main_menu = Menu([
    MenuItem('1', 'New Game', commands.new_game),
    MenuItem('2', 'Load Game', commands.load_game),
    MenuItem('3', 'Exit Game', commands.exit_game)
])

new_game = Menu([
    MenuItem('1', 'Reenter name', commands.get_username),
    MenuItem('2', 'Continue,', commands.continue_),
    MenuItem('3', 'Save', commands.save),
    MenuItem('Q', 'Quit', commands.quit)
])
