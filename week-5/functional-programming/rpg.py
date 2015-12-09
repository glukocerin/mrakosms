class Character:
    def __init__(self, health = 20, armor = 10):
        self._health = health
        self._armor = armor
        self._isAlive = True

    def sufferDamage(self, damage):
        sufferedDamage = self._health + self._armor - damage

        if sufferedDamage < 1:
            self._isAlive = False

    def heal(self, heal):
        self._health += heal

    def getHealt(self):
        return self._health

    def isAlive(self):
        return self._isAlive

def handleEvents(events):
    list(map(handleEvent , events))

def handleEvent(event):
    eventHandlers[event['type']](event)

def applyHeal(event):
    event['character'].heal(event['size'])

def applyDamage(event):
    event['character'].sufferDamage(event['size'])

eventHandlers = {
    'damage': applyDamage,
    'heal': applyHeal
}


### EXCERSIZE ###

# Very ugly!!!
# list(map(lambda event : event['character'].sufferDamage(event['size']), list(filter(lambda event: event['type'] == 'damage', events))))
# list(map(lambda event: eventHandlers[event['type']](event) , events))

    # damagelist = list(filter(lambda event: event['type'] == 'damage', events))
    # healtlist = list(filter(lambda event: event['type'] == 'heal', events))



    # [event['character'].heal(event['size']) for event in healtlist]
    # [event['character'].sufferDamage(event['size']) for event in damagelist]

    # list(map(lambda event : event['character'].sufferDamage(event['size']),damagelist))

    # for event in damagelist:
    #     event['character'].sufferDamage(event['size'])

    # [event['character'].sufferDamage(event['size']) for event in damagelist]

# def handleHealEvents(events):
#     # healtlist = list(filter(lambda event: event['type'] == 'heal', events))
#     # list(map(lambda event : event['character'].heal(event['size']),healtlist))
#
#     healtlist = []
#     for event in events:
#         if event['type'] == 'heal':
#             healtlist.append(event)
#
#     # for event in healtlist:
#     #     event['character'].heal(event['size'])
#     [event['character'].heal(event['size']) for event in healtlist]
