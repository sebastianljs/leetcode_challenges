import unittest
from leetcode_challenges.palindrome_pairs import Solution

class TestPalindromePairs(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_palindrome_pair_empty(self):
        self.assertIsNone(self.solution.palindrome_pairs([]))

    def test_palindrome_pair_list_with_empty_str(self):
        test_words = ["", ""]
        expected_pairs = [[0, 1], [1, 0]]
        self.assertListEqual(expected_pairs, self.solution.palindrome_pairs(test_words))

class TestIsPalindrome(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_string(self):
        self.assertTrue(self.solution._is_palindrome(""))

    def test_is_palindrome_true(self):
        self.assertTrue(self.solution._is_palindrome("aba"))
        test_word = "hello"
        test_palindrome = test_word + test_word[::-1]
        self.assertTrue(self.solution._is_palindrome(test_palindrome))

    def test_is_palindrome_false(self):
        test_word = "aloha"
        self.assertFalse(self.solution._is_palindrome(test_word))

