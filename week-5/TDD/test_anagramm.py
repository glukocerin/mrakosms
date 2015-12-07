import unittest
from anagramm import is_anagramm

class TestIsAnagramm(unittest.TestCase):
    def test_is_anagramm(self):
        self.assertEqual(is_anagramm('', ''), True)
        self.assertEqual(is_anagramm('a',''), False)
        self.assertEqual(is_anagramm('ab','ba'), True)
        self.assertEqual(is_anagramm('abc','bac'), True)
        self.assertEqual(is_anagramm('abcdef','ecfbda'), True)

unittest.main()
