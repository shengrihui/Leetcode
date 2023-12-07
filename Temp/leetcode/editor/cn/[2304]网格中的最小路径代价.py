# 2304 网格中的最小路径代价
from math import *
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(m - 2, -1, -1):
            for j in range(n):
                # 计算从 grid[i][j] 到 grid[i+1][k] 的最小代价，并直接加到 grid[i][j] 上
                mn = inf
                t = grid[i][j]
                for k in range(n):
                    c = grid[i + 1][k] + moveCost[t][k]
                    mn = c if c < mn else mn
                grid[i][j] += mn
        return min(grid[0])
# leetcode submit region end(Prohibit modification and deletion)
