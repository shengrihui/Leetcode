# 994 腐烂的橘子
# https://leetcode.cn/problems/rotting-oranges/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        fresh = {(x, y) for x in range(n) for y in range(m) if grid[x][y] == 1}
        unfresh = {(x, y) for x in range(n) for y in range(m) if grid[x][y] == 2}
        if not unfresh and fresh:
            return -1
        if not fresh and unfresh or not fresh and not unfresh:
            return 0
        flag = True
        t = 0
        while flag:
            flag = False
            for x, y in unfresh.copy():
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nx, ny = x + dx, y + dy
                    if (nx, ny) in fresh:
                        unfresh.add((nx, ny))
                        flag = True
                        fresh.remove((nx, ny))
            t += flag
        return t if not fresh else -1
# leetcode submit region end(Prohibit modification and deletion)
