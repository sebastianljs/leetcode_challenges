import unittest
from leetcode_challenges.remove_duplicates import Solution

class TestRemoveDuplicates(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_remove_duplicates(self):
        test_str = "aabbccc"
        expected = "abc"
        self.assertEqual(expected, self.solution.remove_duplicates(test_str))