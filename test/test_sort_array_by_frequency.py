import unittest
from leetcode_challenges.sort_array_by_frequency import Solution

class TestSortArrayByFrequency(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_sort_array_empty(self):
        self.assertEqual([], self.solution.sort_by_frequency([]))

    def test_sort_array(self):
        test_arr = [0, 1, 2, 2, 3]
        expected = [2, 2, 0, 1, 3]
        self.assertListEqual(expected, self.solution.sort_by_frequency(test_arr))

    def test_sort_array_big(self):
        test_arr = [0, 10, 10, 10, 2, 2, 30, 30, 30, 30]
        expected = [30, 30, 30, 30, 10, 10, 10, 2, 2, 0]
        self.assertListEqual(expected, self.solution.sort_by_frequency(test_arr))