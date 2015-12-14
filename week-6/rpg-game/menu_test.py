import unittest
from menu import *

class MenuTest(unittest.TestCase):
    def test_main_menu(self):
        self.assertEqual(main_menu('N'), None)
        self.assertEqual(main_menu('L'), None)
        self.assertEqual(main_menu('E'), None)

    def test_sub_menu_new_game(self):
        self.assertEqual(sub_menu_new_game(''), None)

    def test_sub_menu_load_game(self):
        self.assertEqual(sub_menu_load_game(''), None)

unittest.main()

