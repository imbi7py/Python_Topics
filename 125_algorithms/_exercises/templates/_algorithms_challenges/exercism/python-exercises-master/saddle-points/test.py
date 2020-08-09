"""Tests for the saddle-points exercise

Implementation note:
The saddle_points function must validate the input matrix and raise a
ValueError with a meaningful error message if the matrix turns out to be
irregular.
"""
______ unittest

from saddle_points ______ saddle_points


class SaddlePointTest(unittest.TestCase
    ___ test_one_saddle(self
        inp = [[9, 8, 7], [5, 3, 2], [6, 6, 7]]
        self.assertEqual(saddle_points(inp), set([(1, 0)]))

    ___ test_no_saddle(self
        self.assertEqual(saddle_points([[2, 1], [1, 2]]), set())

    ___ test_mult_saddle(self
        inp = [[5, 3, 5, 4], [6, 4, 7, 3], [5, 1, 5, 3]]
        ans = set([(0, 0), (0, 2), (2, 0), (2, 2)])
        self.assertEqual(saddle_points(inp), ans)

    ___ test_empty_matrix(self
        self.assertEqual(saddle_points([]), set())

    ___ test_irregular_matrix(self
        inp = [[3, 2, 1], [0, 1], [2, 1, 0]]
        self.assertRaises(ValueError, saddle_points, inp)


__ __name__ __ '__main__':
    unittest.main()
