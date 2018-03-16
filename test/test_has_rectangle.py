import unittest

from leetcode_challenges.has_rectangle import Solution


class HasRectangleTest(unittest.TestCase):
    def test_has_rectangle_error(self):
        with self.assertRaises(ValueError):
            Solution.has_rectangle([1, 2])

    def test_has_rectangle_empty(self):
        self.assertFalse(Solution.has_rectangle([]))
        self.assertFalse(Solution.has_rectangle([[]]))

    def test_has_rectangle_one_row(self):
        self.assertFalse(Solution.has_rectangle([[1 for _ in range(10)]]))

    def test_has_rectangle_all_zeroes(self):
        test_matrix = [[0 for _ in range(3)] for _ in range(6)]
        self.assertFalse(Solution.has_rectangle(test_matrix))

    def test_has_rectangle_all_ones(self):
        test_matrix = [[1 for _ in range(3)] for _ in range(13)]
        self.assertTrue(Solution.has_rectangle(test_matrix))

    def test_has_rectangle_small_false(self):
        test_matrix = [[1, 0, 1],
                       [0, 1, 0],
                       [0, 0, 0]]
        self.assertFalse(Solution.has_rectangle(test_matrix))

    def test_has_rectangle_small_true(self):
        test_matrix = [[1, 1, 1],
                       [0, 1, 0],
                       [1, 0, 1]]
        self.assertTrue(Solution.has_rectangle(test_matrix))


if __name__ == "__main__":
    unittest.main()
