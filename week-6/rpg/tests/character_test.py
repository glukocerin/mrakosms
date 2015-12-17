import unittest
import os, sys
lib_path = os.path.abspath(os.path.join('..'))
sys.path.append(lib_path)
from character import Character

class CharacterTest(unittest.TestCase):
    def setUp(self):
        self.user = Character()
        self.user.name = 'testname'
        self.user.set_stats()
        self.user.set_start_stats()

    def test_instantiate(self):
        self.assertIsInstance(Character(), Character)

    def test_get_username(self):
        self.assertEqual(self.user.get_username(), 'testname')

    def test_dice(self):
        self.assertIn(Character.dice(self, 1), range(7))
        self.assertIn(Character.dice(self, 2), range(13))

    def test_set_stats(self):
        self.assertIn(self.user.stats['Health'], range(25))

    def test_set_start_stats(self):
        self.assertEqual(self.user.stats, self.user.start_stats)





unittest.main()
