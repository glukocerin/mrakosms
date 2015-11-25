# http://www.codewars.com/kata/556cebcf7c58da564a000045/train/python
#
# Given a grid of size m x n, calculate the total number of rectangles contained in this rectangle. All integer sizes and positions are counted.
#
# Examples:
#
# numberOfRectangles(3, 2) == 18
# numberOfRectangles(4, 4) == 100

# ver 1
def number_of_rectangles(m, n):
    rectangles = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            rectangles += (1 + n - j) * ( 1 + m - i)
    return rectangles

# ver 2 - http://www.gottfriedville.net/mathprob/comb-subrect.html
# def number_of_rectangles(m, n):
#     return (m * (m + 1) * n * (n + 1)) / 4


# Test cases
#
# Test.assert_equals(number_of_rectangles(4, 4), 100, "Should be 100")
# Test.assert_equals(number_of_rectangles(5, 5), 225, "Should be 225")
