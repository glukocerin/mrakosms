import unittest
import os, sys
lib_path = os.path.abspath(os.path.join('..'))
sys.path.append(lib_path)
from player import Player

class CharacterTest(unittest.TestCase):
    def setUp(self):
        self.player = Player()
        self.player.name = 'testplayer'
        self.player.set_stats()
        self.player.set_start_stats()

    def test_instantiate(self):
        self.assertIsInstance(Player(), Player)

    def test_get_username(self):
        self.assertEqual(self.player.get_username(), 'testplayer')
