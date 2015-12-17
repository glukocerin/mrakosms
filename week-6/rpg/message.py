class Message:
    def __init__(self, message):
        self.message = message

    def show(self):
        print(self.message)

    def ret(self):
        return self.message

### Menu Items Messages

choose = Message('\nFrom the number of menu above choose one: ')
continue_ = Message('Continue')
save = Message('Save')
quit = Message('Quit')
wrong_integer = Message('Wrong input, please select from menu numbers!')
no_integer = Message('Wrong, that was no integer!')


# Main Menu
new_game = Message('New Game')
load_game = Message('Load Game')
exit_game = Message('Exit')
exit = Message('Are you sure? (y)es / (n)o: ')

# New Game Menu
set_name = Message('Enter name: ')
name_is_correct = Message('Is it correct? ->')
reenter_name = Message('Reenter name')

# Roll Menu
reroll_stats = Message('Reroll stats')
start_roll = Message('Your started stats are the following:')

# Quit menu
quit_question = Message('Quit menu')
save_and_quit = Message('Save and Quit')
save_wo_quit = Message('Quit without Save')
resume = Message('Resume')

#Potion
choose_potion = Message('Choose a potion')
potion_of_health = Message('Potion of Health')
potion_of_dexterity = Message('Potion of Dexterity')
potion_of_luck = Message('Potion of Luck')
set_potion = Message('Your selected:')
reselect_potion = Message('Reselect the Potion')
begin = Message('Begin')
inventory = Message('Your inventory:')
your_name = Message('Name: ')

begin_welcome = Message('\nYour stats are the following:')
begin_fight = Message('Test your Sword in a test fight')
