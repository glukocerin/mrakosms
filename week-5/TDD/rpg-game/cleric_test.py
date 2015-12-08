import unittest
from character import Character
from cleric import Cleric


class TestCleric(unittest.TestCase):
    def test_existance(self):
        cleric = Cleric('TestHerlic', 100, 10)

    def test_inheritance(self):
        cleric = Cleric('TestHerlic', 100, 10)
        self.assertEqual(cleric.hp, 100)

    def test_can_heal(self):
        character = Character('Test', 100, 10)
        cleric = Cleric('TestCleric', 100, 10)
        cleric.heal(character)
        self.assertEqual(character.hp, 110)

unittest.main()
