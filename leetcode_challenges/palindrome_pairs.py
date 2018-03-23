class Solution(object):
    def palindrome_pairs(self, words):
        """
        :type words: list[str]
        :rtype: list[list[int]]
        """

    def _is_palindrome(self, word):
        left, right = 0, len(word) - 1
        while left <= right:
            if word[left] != word[right]:
                return False
            left += 1
            right -= 1
        return True

