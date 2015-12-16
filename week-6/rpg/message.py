class Message:
    def __init__(self, message):
        self.message = message

    def show(self):
        print(self.message)

    def ret(self):
        return self.message





choose = Message(
    'Valassz egy szamot, majd nyomj egy Entert: '
    )
wrong_integer = Message(
    'Nem jo szamot adtal meg, mert nem szerepel a menuben!!!\nNezd meg ujra a menut es probalkozz , hatha beletalalsz'
    )
no_integer = Message(
    'Ez nem szam volt, probald ujra'
    )
add_name = Message(
    'Hogy hivhatunk a jatekban?: '
    )

quit = Message(
    'Hogy szeretnel kilepni?: '
    )

exit = Message(
    'Biztos ki szeretnel lepni? (y - igen, n - nem): '
        )

dexterity_roll = Message(
    'Ez itt jelenik meg'
    )

roll_one = Message(
    'Dobj a kockaval'
        )

choose_potion = Message(
    'Valassz egy italt, amit majd a jatek soran hasznalhatsz fel'
    )

new_game = Message(
    '- Uj jatek inditasa'
    )

load_game = Message(
    '- Mentett jatek betoltese'
    )

exit_game = Message(
    '- Kilepes a jatekbol')
set_potion = Message(
    'Az alabbi potiont valsztottad amit majd felhasnalhatsz a jatek soran:')

potion_of_health = Message(
    'Potion of Health'
    )

potion_of_dexterity = Message(
    'Potion of Dexterity'
    )
potion_of_luck = Message(
    'Potion of Luck'
    )
