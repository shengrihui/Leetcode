# 73 矩阵置零
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        c = r = 0
        for i, row in enumerate(matrix):
            for j, x in enumerate(row):
                if x == 0:
                    if c >> j & 1 == 0:
                        c += 1 << j
                    if r >> i & 1 == 0:
                        r += 1 << i
        j = 0
        while j <= cols:
            if c >> j & 1:
                for i in range(rows):
                    matrix[i][j] = 0
            j += 1
        i = 0
        while i <= rows:
            if r >> i & 1:
                for j in range(cols):
                    matrix[i][j] = 0
            i += 1
# leetcode submit region end(Prohibit modification and deletion)
