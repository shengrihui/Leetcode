# 第 397 场周赛 第 3 题
# 题目：100281. 矩阵中的最大得分
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-397/problems/maximum-difference-score-in-a-grid/
# 题库：https://leetcode.cn/problems/maximum-difference-score-in-a-grid

from math import inf
from typing import List


# https://leetcode.cn/problems/maximum-difference-score-in-a-grid/solutions/2821797/yuan-di-xiu-gai-jie-sheng-kong-jian-by-w-tnc1
class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        ans = -inf

        mx = grid[-1][-1]
        for i in range(n - 2, -1, -1):
            if mx - grid[i][-1] > ans:
                ans = mx - grid[i][-1]
            if grid[i][-1] > mx:
                mx = grid[i][-1]
            grid[i][-1] = mx

        mx = grid[-1][-1]
        for j in range(m - 2, -1, -1):
            if mx - grid[-1][j] > ans:
                ans = mx - grid[-1][j]
            if grid[-1][j] > mx:
                mx = grid[-1][j]
            grid[-1][j] = mx

        for i in range(n - 2, -1, -1):
            for j in range(m - 2, -1, -1):
                t = grid[i][j + 1] if grid[i][j + 1] > grid[i + 1][j] else grid[i + 1][j]
                if t - grid[i][j] > ans:
                    ans = t - grid[i][j]
                if t > grid[i][j]:
                    grid[i][j] = t
        return ans


s = Solution()
examples = [
    (dict(grid=[[6, 3, 2, 2], [7, 2, 4, 3], [3, 1, 3, 2]]), 2),
    (dict(grid=[[6, 1, 4, 6], [5, 6, 3, 5], [5, 3, 10, 3], [8, 7, 1, 5], [1, 6, 6, 2]]), 9),
    (dict(grid=[[6, 5, 1], [5, 7, 9], [6, 7, 4], [6, 10, 5]]), 8),
    (dict(grid=[[9, 5, 7, 3], [8, 9, 6, 1], [6, 7, 14, 3], [2, 5, 3, 1]]), 9),
    (dict(grid=[[4, 3, 2], [3, 2, 1]]), -1),
]
for e, a in examples:
    print(a, e)
    print(s.maxScore(**e))
