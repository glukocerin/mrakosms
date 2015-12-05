import sudoku_checker
import unittest

class TestSudokuChecker(unittest.TestCase):
    def test_is_complete_empty(self):
        test_input = []
        expected = False
        actual = sudoku_checker.is_complete(test_input)
        self.assertEqual(expected, actual, "The row is empty.")

    def test_is_complete_too_short(self):
        test_input = [1, 2, 3, 4, 5, 6, 7, 8]
        expected = False
        actual = sudoku_checker.is_complete(test_input)
        self.assertEqual(expected, actual, "The row is too short.")

    def test_is_complete_too_long(self):
        test_input = [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12]
        expected = False
        actual = sudoku_checker.is_complete(test_input)
        self.assertEqual(expected, actual, "The row is too long.")

    def test_is_complete_sorted_first_is_1(self):
        test_input = [0, 2, 3, 4, 5, 6, 7, 8, 9]
        expected = False
        actual = sudoku_checker.is_complete(test_input)
        self.assertEqual(expected, actual, "The row firs element not 1 ")

    def test_is_complete_sorted_invalid_char(self):
        test_input = [0, 2, 3, 4, 5, 6, 7, 'x', 9]
        expected = False
        actual = sudoku_checker.is_complete(test_input)
        self.assertEqual(expected, actual, "Invalid char ")

    def test_is_complete_integer_item(self):
        test_input = [1, 2, 3.6, 4, 5, 6, 7, 8, 9]
        expected = False
        actual = sudoku_checker.is_complete(test_input)
        self.assertEqual(expected, actual, "The row elements is not int ")

    def test_is_complete_sum(self):
        test_input = [1, 1, 3, 4, 5, 6, 7, 8, 9]
        expected = False
        actual = sudoku_checker.is_complete(test_input)
        self.assertEqual(expected, actual, "The row sum not 45")

    def test_is_complete_true_check(self):
        test_input = [9, 1, 3, 4, 5, 6, 7, 8, 2]
        expected = True
        actual = sudoku_checker.is_complete(test_input)
        self.assertEqual(expected, actual, "Not ok")

    def test_done_or_not_random_correct(self):
        test_input = [[1, 3, 2, 5, 7, 9, 4, 6, 8]
                    ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                    ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                    ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                    ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                    ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                    ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                    ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                    ,[8, 7, 9, 6, 4, 2, 1, 5, 3]]
        expected = 'Finished'
        actual = sudoku_checker.done_or_not(test_input)
        self.assertEqual(expected, actual, "Correct")

    def test_done_or_not_random_incorrect(self):
        test_input = [[1, 3, 2, 5, 7, 9, 4, 6, 8]
                ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                ,[8, 7, 9, 6, 4, 2, 1, 3, 5]]
        expected = 'Try again!'
        actual = sudoku_checker.done_or_not(test_input)
        self.assertEqual(expected, actual, "Incorrect")

    def test_get_reghion_middle_region(self):
        test_input = [[1, 3, 2, 5, 7, 9, 4, 6, 8]
                ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                ,[8, 7, 9, 6, 4, 2, 1, 3, 5]]
        expected = [1, 5, 8, 7, 9, 3, 4, 2, 6]
        actual = sudoku_checker.get_region(test_input, 1, 1)
        self.assertEqual(expected, actual, "return middle element")





unittest.main()
