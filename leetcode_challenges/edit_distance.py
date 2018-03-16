import logging
from pprint import pformat
import argparse

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
sh = logging.StreamHandler()
sh.setLevel(logging.DEBUG)
logger.addHandler(sh)


class Solution:
    def __init__(self):
        pass

    @staticmethod
    def min_distance(word1, word2):
        word1_len = len(word1)
        word2_len = len(word2)
        distance_matrix = [[0 for _ in range(word2_len + 1)] for _ in range(word1_len + 1)]
        for i in range(word1_len + 1):
            distance_matrix[i][0] = i
        for j in range(word2_len + 1):
            distance_matrix[0][j] = j
        logger.info(pformat(distance_matrix))
        for i in range(1, word1_len + 1):
            for j in range(1, word2_len + 1):
                if word1[i - 1] == word2[j-1]:
                    distance_matrix[i][j] = distance_matrix[i - 1][j - 1]
                else:
                    distance_matrix[i][j] = min(distance_matrix[i - 1][j - 1] + 1, 
                                                distance_matrix[i][j - 1] + 1,
                                                distance_matrix[i - 1][j] + 1)
                logger.debug(pformat(distance_matrix))
        return distance_matrix[word1_len][word2_len]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-w1", "--word1", dest="word1", required=True)
    parser.add_argument("-w2", "--word2", dest="word2", required=True)
    args = parser.parse_args()
    solution = Solution()
    solution.min_distance(**vars(args))


if __name__ == "__main__":
    main()

