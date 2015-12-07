import unittest
from barbarian import Barbarian
from character import Character

class TestBarbarian(unittest.TestCase):
    def test_existance(self):
        barbarian = Barbarian('Test', 100, 10)

    def test_strike(self):
        barbarian = Barbarian('TestBarbarian', 100, 10)
        enemy = Character('TestEnemy', 100, 10)
        barbarian.strike(enemy)
        self.assertEqual(enemy.hp, 80)

unittest.main()
