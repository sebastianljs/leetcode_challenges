import unittest

from leetcode_challenges.find_median_in_stream import Solution


class TestFindMedianInStream(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()

    def test_find_median_stream(self):
        self.solution.add_to_stream(1)
        self.assertEqual(self.solution.find_median_in_stream(), 1)
        self.solution.add_to_stream(2)
        self.assertAlmostEqual(self.solution.find_median_in_stream(), 1.5)
        self.solution.add_to_stream(3)
        self.assertEqual(self.solution.find_median_in_stream(), 2)
        self.solution.add_to_stream(100)
        self.assertAlmostEqual(self.solution.find_median_in_stream(), 2.5)

