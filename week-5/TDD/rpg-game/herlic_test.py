import unittest
from character import Character
from herlic import Herlic


class TestHerlic(unittest.TestCase):
    def test_existance(self):
        herlic = Herlic('TestHerlic', 100, 10)

    def test_can_heal(self):
        character = Character('Test', 100, 10)
        herlic = Herlic('TestHerlic', 100, 10)
        herlic.heal(character)
        self.assertEqual(character.hp, 110)

unittest.main()
