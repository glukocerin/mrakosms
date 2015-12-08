import random
class Weapon:
    def strike(self, warrior, opponent):
        warrior.hp -= self.self_damage()
        opponent.hp -= self.damage()

    def damage(self):
        raise 'Not implemented'

    def self_damage(self):
        raise 'Not implemented'

class Sword(Weapon):
    def damage(self):
        return 10

    def self_damage(self):
        return 0

class Gun(Weapon):
    def damage(self):
        return 22

    def self_damage(self):
        return 20

class CriticalSword(Weapon):
    def damage(self):
        return 10 + random.randint(0, 10)

    def self_damage(self):
        return 0

class Magic(Weapon):
    def __init__(self, weapon):
        self.weapon = weapon

    def damage(self):
        return self.weapon.damage() * 2

    def self_damage(self):
        return self.weapon.damage() / 2

class Warrior:
    def __init__(self, weapon):
        self.hp = 100
        self.weapon = weapon

    def strike(self, opponent):
        self.weapon.strike(self, opponent)

    def __repr__(self):
        return 'Warrior HP: {}'.format(self.hp)


monster = Warrior(Gun())
warrior = Warrior(Magic(Sword()))

print(warrior)
print(monster)
monster.strike(warrior)
print(warrior)
print(monster)
