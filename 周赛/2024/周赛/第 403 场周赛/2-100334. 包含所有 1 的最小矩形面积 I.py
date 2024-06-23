# 第 403 场周赛 第 2 题
# 题目：100334. 包含所有 1 的最小矩形面积 I
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-403/problems/find-the-minimum-area-to-cover-all-ones-i/
# 题库：https://leetcode.cn/problems/find-the-minimum-area-to-cover-all-ones-i

from typing import List

"""
class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        rows = [sum(row) for row in grid]
        up, down = 0, n
        for i in range(n):
            if rows[i] > 0:
                up = i
                break
        for i in range(n - 1, -1, -1):
            if rows[i] > 0:
                down = i
                break
        cols = [sum(col) for col in zip(*grid)]
        left, right = 0, m
        for i in range(m):
            if cols[i] > 0:
                left = i
                break
        for i in range(m - 1, -1, -1):
            if cols[i] > 0:
                right = i
                break
        return (down - up + 1) * (right - left + 1)
"""


# 灵神
class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        left, right = len(grid[0]), 0
        up, down = len(grid), 0
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x:
                    left = min(left, j)
                    right = max(right, j)
                    up = min(up, i)
                    down = i
        return (right - left + 1) * (down - up + 1)


s = Solution()
examples = [
    (dict(grid=[[0, 1, 0], [1, 0, 1]]), 6),
    (dict(grid=[[0, 0], [1, 0]]), 1),
]
for e, a in examples:
    print(a, e)
    print(s.minimumArea(**e))
