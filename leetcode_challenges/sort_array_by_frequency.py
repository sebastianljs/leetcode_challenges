from collections import Counter
class Solution(object):
    def sort_by_frequency(self, arr):
        num_to_freq = Counter(arr)
        arr.sort(key=lambda x: (-num_to_freq[x], x))
        return arr

