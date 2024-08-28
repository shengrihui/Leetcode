# 3142 判断矩阵是否满足条件
# https://leetcode.cn/problems/check-if-grid-satisfies-conditions/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        n, m = len(grid), len(grid[0])
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if i < n - 1 and grid[i][j] != grid[i + 1][j] or j < m - 1 and grid[i][j] == grid[i][j + 1]:
                    return False
        return True


"""
class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if j and x == row[j - 1] or i and x != grid[i - 1][j]:
                    return False
        return True
"""
# leetcode submit region end(Prohibit modification and deletion)
