class Pirate:
    def __init__(self):
        self.rum = 0

    def drink_rum(self):
        self.rum += 1

    def hows_going_mate(self):
        if self.rum >= 5:
            return 'Arrrrrr'
        else:
            return 'Nothin\''

pirate = Pirate()

pirate.drink_rum()
pirate.drink_rum()
pirate.drink_rum()
pirate.drink_rum()
# pirate.drink_rum()

print(pirate.hows_going_mate())
