import unittest
import os, sys
lib_path = os.path.abspath(os.path.join('..'))
sys.path.append(lib_path)
from menu import Menu

class MenuTest(unittest.TestCase):
    def test_instantiate(self):
        self.assertIsInstance(Menu(''), Menu)




unittest.main()
