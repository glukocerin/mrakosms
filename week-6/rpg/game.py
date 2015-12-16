
from menu import Menu, MenuItem
from menu_item import main_menu
import commands
import curses


commands.clear()
print()
print(20 * '*')
print()
main_menu.display()

# myscreen = curses.initscr()


# myscreen.border(0)
# myscreen.addstr(12, 25, "Python curses in action!")
# myscreen.refresh()
# myscreen.getch()

# curses.endwin()

