# 54 螺旋矩阵
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row, col = len(matrix), len(matrix[0])
        n = row * col
        ans = []
        i = j = 0
        DIR = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d = 0
        si = sj = 0
        ei, ej = row - 1, col - 1
        while si <= i <= ei and sj <= j <= ej:
            ans.append(matrix[i][j])
            if d == 0 and j == ej:
                si += 1
                d = 1
            elif d == 1 and i == ei:
                ej -= 1
                d = 2
            elif d == 2 and j == sj:
                ei -= 1
                d = 3
            elif d == 3 and i == si:
                sj += 1
                d = 0
            di, dj = DIR[d]
            i, j = i + di, j + dj
        return ans

# leetcode submit region end(Prohibit modification and deletion)
