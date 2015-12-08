import unittest
from character import Character
from wizard import Wizard


class TestWizard(unittest.TestCase):
    def test_existance(self):
        wizard = Wizard('TestWizard', 100, 10, 10)

    def test_inheritance(self):
        wizard = Wizard('TestWizard', 100, 10, 10)
        self.assertEqual(wizard.hp, 100)

    def test_has_manna_property(self):
        wizard = Wizard('TestWizard', 100, 10, 10)
        self.assertEqual(wizard.manna, 10)

    def test_manna_week(self):
        wizard = Wizard('TestWizard', 100, 10, 4)
        enemy = Character('TestCharacter', 100, 10)
        wizard.strike(enemy)
        self.assertEqual(wizard.manna, 4)

    def test_manna_strong(self):
        wizard = Wizard('TestWizard', 100, 10, 15)
        enemy = Character('TestCharacter', 100, 10)
        wizard.strike(enemy)
        self.assertEqual(wizard.manna, 10)

    def test_strike_manna_week(self):
        wizard = Wizard('TestWizard', 100, 9, 4)
        enemy = Character('TestCharacter', 100, 10)
        wizard.strike(enemy)
        self.assertEqual(enemy.hp, 97)

    def test_strike_manna_strong(self):
        wizard = Wizard('TestWizard', 100, 10, 10)
        enemy = Character('TestCharacter', 100, 10)
        wizard.strike(enemy)
        self.assertEqual(enemy.hp, 70)

unittest.main()
