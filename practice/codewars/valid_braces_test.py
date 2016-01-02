import unittest
from valid_braces import valid_braces

class ValidBracesTest(unittest.TestCase):
    def test_odd_brace(self):
        self.assertFalse(valid_braces('('))
        self.assertFalse(valid_braces(')'))
        self.assertFalse(valid_braces('{'))
        self.assertFalse(valid_braces('}'))
        self.assertFalse(valid_braces('['))
        self.assertFalse(valid_braces(']'))

    def test_single_braces(self):
        self.assertTrue(valid_braces('{}'))
        self.assertTrue(valid_braces('[]'))
        self.assertTrue(valid_braces('()'))

    def test_double_braces(self):
        self.assertTrue(valid_braces('()()'))
        self.assertTrue(valid_braces('(){}'))
        self.assertTrue(valid_braces('()[]'))

    def test_double_nested_braces(self):
        self.assertTrue(valid_braces('(())'))
        self.assertTrue(valid_braces('({})'))

    # def test_1(self):
    #     self.assertTrue(valid_braces('(){}[]'))


# validBraces( "(){}[]" ) => returns true
# validBraces( "(}" ) => returns false
# validBraces( "[(])" ) => returns false
# validBraces( "([{}])" ) => returns true

unittest.main()
