from collections import defaultdict


class Solution(object):
    @staticmethod
    def has_rectangle(matrix):
        if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
            raise ValueError("matrix must be a 2D matrix")

        combo_table = defaultdict(set)
        n_rows = len(matrix)
        if n_rows == 0:
            return False
        n_cols = len(matrix[0])
        for i in range(n_rows):
            for j in range(n_cols):
                for k in range(j + 1, n_cols):
                    if matrix[i][j] == matrix[i][k] == 1:
                        if (j in combo_table and k in combo_table[j]) or \
                           (k in combo_table and j in combo_table[k]):
                            return True

                        combo_table[j].add(k)
                        combo_table[k].add(j)
        return False
