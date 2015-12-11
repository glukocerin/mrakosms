import unittest
from duplicate_encoder import Encoder

class TestEncoder(unittest.TestCase):
    def setUp(self):
        self.word = 'din'
    def test_instantiate(self):
        self.assertIsInstance(Encoder(self.word), Encoder)
    def test_characters_transform(self):
        self.assertEqual(Encoder.duplicate_encode('din'), '(((')
    def test_characters_duplicated(self):
        self.assertEqual(Encoder.duplicate_encode('rece'), '()()')
    def test_characters_upper_and_lower(self):
        self.assertEqual(Encoder.duplicate_encode("Success"), ')())())')
    def test_characters_space(self):
        self.assertEqual(Encoder.duplicate_encode("Suc cess"), ')()()())')
    def test_characters_special_char(self):
        self.assertEqual(Encoder.duplicate_encode("Suc#cess"), ')()()())')

unittest.main()
