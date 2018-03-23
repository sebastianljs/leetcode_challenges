import unittest
from leetcode_challenges.minimum_delete_sum import Solution

class TestMinimumDeleteSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty(self):
        self.assertEqual(0, self.solution.minimum_delete_sum("", ""))

    def test_one_word_empty(self):
        test_word = "john"
        test_word_ascii_sum = sum(ord(c) for c in test_word)
        self.assertEqual(test_word_ascii_sum, self.solution.minimum_delete_sum("", test_word))
        self.assertEqual(test_word_ascii_sum, self.solution.minimum_delete_sum(test_word, ""))

    def test_word_equal(self):
        test_word = "jane"
        self.assertEqual(0, self.solution.minimum_delete_sum(test_word, test_word))

    def test_word1_is_subset_word2(self):
        test_word1 = "john"
        addition = "son"
        test_word2 = test_word1 + addition
        ascii_sum = sum(ord(c) for c in addition)
        self.assertEqual(ascii_sum, self.solution.minimum_delete_sum(test_word1, test_word2))

    def test_word1_word2_no_overlap(self):
        test_word1 = "abc"
        test_word2 = "def"
        ascii_sum = sum(ord(c) for c in (test_word1 + test_word2))
        self.assertEqual(ascii_sum, self.solution.minimum_delete_sum(test_word1, test_word2))

    def test_word1_word2_partial_overlap(self):
        test_word1 = "latte"
        test_word2 = "omelette"
        ascii_sum = sum(ord(c) for c in "omeea")
        self.assertEqual(ascii_sum, self.solution.minimum_delete_sum(test_word1, test_word2))

    def test_transitive(self):
        test_word1 = "matthew"
        test_word2 = "michael"
        self.assertEqual(self.solution.minimum_delete_sum(test_word1, test_word2),
                         self.solution.minimum_delete_sum(test_word2, test_word1))