import unittest
from leetcode_challenges.edit_distance import Solution

class TestEditDistance(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_edit_distance_same_word(self):
        test_word = "abcdef ghij"
        self.assertEqual(0, self.solution.min_distance(test_word, test_word))

    def test_edit_distance_empty_word(self):
        self.assertEqual(0, self.solution.min_distance("", ""))

    def test_edit_distance_one_word_empty(self):
        test_word = "teapot"
        self.assertEqual(len(test_word), self.solution.min_distance(test_word, ""))
        self.assertEqual(len(test_word), self.solution.min_distance("", test_word))

    def test_edit_distance_different_words(self):
        test_word_1_list = ["abbc", "cabb"]
        test_word_2_list = ["bbac", "bbca"]
        expected_min_distance = [2, 4]
        computed_min_distance = [self.solution.min_distance(w1, w2) for w1, w2 in zip(test_word_1_list, test_word_2_list)]
        self.assertListEqual(expected_min_distance, computed_min_distance)

if __name__ == "__main__":
    unittest.main()