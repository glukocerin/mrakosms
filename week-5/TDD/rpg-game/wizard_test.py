import unittest
from character import Character
from wizard import Wizard


class TestWizard(unittest.TestCase):
    def test_existance(self):
        wizard = Wizard('TestWizard', 100, 10, 10)

    def test_has_manna_property(self):
        wizard = Wizard('TestWizard', 100, 10, 10)
        self.assertEqual(wizard.manna, 10)

    def test_strike_and_manna(self):
        wizard = Wizard('TestWizard', 100, 10, 5)
        enemy = Character('TestCharacter', 100, 10)
        wizard.strike(enemy)
        self.assertEqual(enemy.hp, 90)
        self.assertEqual(wizard.manna, 0)

    def test_manna_strong(self):
        wizard = Wizard('TestWizard', 100, 10, 10)
        enemy = Character('TestCharacter', 100, 10)
        wizard.strike(enemy)
        self.assertEqual(enemy.hp, 70)
        self.assertEqual(wizard.manna, 5)

unittest.main()
