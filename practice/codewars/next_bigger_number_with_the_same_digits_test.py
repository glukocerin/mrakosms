import unittest
from next_bigger_number_with_the_same_digits import next_bigger

class NextBiggerTest(unittest.TestCase):
    def test_if_only_one(self):
        self.assertEqual(next_bigger(1), -1)

    def test_11(self):
        self.assertEqual(next_bigger(11), -1)

    def test_12(self):
        self.assertEqual(next_bigger(12), 21)

    def test_123(self):
        self.assertEqual(next_bigger(123), 132)

    def test_21(self):
        self.assertEqual(next_bigger(21), -1)

    def test_321(self):
        self.assertEqual(next_bigger(321), -1)

    def test_2016(self):
        self.assertEqual(next_bigger(2016), 2061)

    def test_980(self):
        self.assertEqual(next_bigger(890), 908)

    def test_1234567890(self):
        self.assertEqual(next_bigger(59853),83559)

unittest.main()
