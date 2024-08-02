# 3128 直角三角形
# https://leetcode.cn/problems/right-triangles/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        sum_row = [sum(row) for row in grid]
        sum_col = [sum(col) for col in zip(*grid)]
        ans = 0
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x == 1:
                    ans += (sum_row[i] - 1) * (sum_col[j] - 1)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
