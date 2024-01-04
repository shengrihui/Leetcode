# 2397 被列覆盖的最多行数
# https://leetcode.cn/problems/maximum-rows-covered-by-columns/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:
        ans = 0
        n, m = len(matrix), len(matrix[0])
        rows = [0 for _ in range(n)]
        for i, row in enumerate(matrix):
            for j, x in enumerate(row):
                rows[i] += x << j

        for s in range(1 << m):
            if s.bit_count() != numSelect:
                continue
            ans = max(ans, sum((r & ~s) == 0 for r in rows))
        return ans
        # rows = [sum(x << j for j, x in enumerate(row)) for row in matrix]
        # return max(sum((r & ~s) == 0 for r in rows) for s in range(1 << len(matrix[0])) if s.bit_count() == numSelect)
# leetcode submit region end(Prohibit modification and deletion)
