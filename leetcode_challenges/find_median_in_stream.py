from heapq import heappush, heappop, heappushpop


class Solution(object):
    def __init__(self):
        self._stream = []
        self._max_heap = []  # smaller heap
        self._min_heap = []  # bigger heap

    def find_median_in_stream(self):
        if len(self._min_heap) > len(self._max_heap):
            return float(self._min_heap[0])
        return (self._min_heap[0] - self._max_heap[0]) / 2.0

    def add_to_stream(self, num):
        heappush(self._max_heap, -heappushpop(self._min_heap, num))
        if len(self._min_heap) < len(self._max_heap):
            heappush(self._min_heap, -heappop(self._max_heap))






