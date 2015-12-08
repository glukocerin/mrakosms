import unittest
from character import Character
from monster import Monster


class TestHerlic(unittest.TestCase):
    def test_existance(self):
        monster = Monster('TestMonster', 100, 10)

    def test_inheritance(self):
        monster = Monster('TestMonster', 100, 10)
        self.assertEqual(monster.hp, 100)

    def test_strike_and_heal(self):
        character = Character('Test', 100, 10)
        monster = Monster('TestMonster', 100, 10)
        monster.strike(character)
        self.assertEqual(character.hp, 90)
        self.assertEqual(monster.hp, 102)

unittest.main()
