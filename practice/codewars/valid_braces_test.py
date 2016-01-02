import unittest
from valid_braces import valid_braces

class ValidBracesTest(unittest.TestCase):
    def test_odd_bracket(self):
        self.assertFalse(valid_braces('('))
        self.assertFalse(valid_braces(')'))
        self.assertFalse(valid_braces('{'))
        self.assertFalse(valid_braces('}'))
        self.assertFalse(valid_braces('['))
        self.assertFalse(valid_braces(']'))

    def test_single_brackets(self):
        self.assertTrue(valid_braces('{}'))
        self.assertTrue(valid_braces('[]'))
        self.assertTrue(valid_braces('()'))

    def test_double_brackets(self):
        self.assertTrue(valid_braces('()()'))
        self.assertTrue(valid_braces('(){}'))
        self.assertTrue(valid_braces('()[]'))

    def test_double_nested_brackets(self):
        self.assertTrue(valid_braces('(())'))
        self.assertTrue(valid_braces('({})'))

    def test_wrong(self):
        self.assertFalse(valid_braces('({}[]'))
        self.assertFalse(valid_braces('(){[]'))
        self.assertFalse(valid_braces('({}}'))
        self.assertFalse(valid_braces('({}['))

unittest.main()
