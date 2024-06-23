# 第 403 场周赛 第 4 题
# 题目：100332. 包含所有 1 的最小矩形面积 II
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-403/problems/find-the-minimum-area-to-cover-all-ones-ii/
# 题库：https://leetcode.cn/problems/find-the-minimum-area-to-cover-all-ones-ii

from math import inf
from typing import List


class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        return min(self.f(grid), self.f(self.rotate(grid)))

    def f(self, grid: List[List[int]]) -> int:
        # [l,r) 左闭右开的区间
        def area(grid: List[List[int]], l: int, r: int) -> tuple[int]:
            left, right = len(grid[0]), 0
            up, down = len(grid), 0
            for i, row in enumerate(grid):
                for j, x in enumerate(row[l:r]):
                    if x:
                        left = min(left, j)
                        right = max(right, j)
                        up = min(up, i)
                        down = i
            return left, right, up, down

        def minimumArea(grid: List[List[int]], l: int, r: int) -> int:
            left, right, up, down = area(grid, l, r)
            return (right - left + 1) * (down - up + 1)

        left, right, up, down = area(grid, 0, len(grid[0]))
        ans = inf
        for i in range(up + 1, down + 1):
            # 三横
            for j in range(i + 1, down + 1):
                a = minimumArea(grid[up:i], left, right + 1)
                a += minimumArea(grid[i:j], left, right + 1)
                a += minimumArea(grid[j:down + 1], left, right + 1)
                ans = min(ans, a)

            for j in range(left + 1, right + 1):
                # 横上下两竖
                a = minimumArea(grid[up:i], left, right + 1)
                a += minimumArea(grid[i:down + 1], left, j)
                a += minimumArea(grid[i:down + 1], j, right + 1)

                # 横下上两竖
                b = minimumArea(grid[up:i], left, j)
                b += minimumArea(grid[up:i], j, right + 1)
                b += minimumArea(grid[i:down + 1], left, right + 1)

                ans = min(ans, a, b)
        return ans

    def rotate(self, grid: List[List[int]]) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        b = [[0] * n for _ in range(m)]
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                b[j][n - 1 - i] = x
        return b


examples = [
    (dict(grid=[[1, 1], [1, 1]]), 4),
    (dict(grid=[[1, 1], [0, 1]]), 3),
    (dict(grid=[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 1, 1, 1]]), 5),
    (dict(grid=[[0, 0, 0, 0, 0], [0, 0, 1, 1, 1], [0, 1, 0, 1, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]), 5),
    (dict(grid=[[0, 0, 0, 0, 0], [0, 0, 0, 0, 1], [0, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 1, 0, 0, 0]]), 5),
    (dict(grid=[[0, 0, 0, 0, 0], [1, 1, 0, 1, 0], [0, 1, 0, 1, 0], [1, 1, 0, 1, 0], [1, 0, 0, 0, 0]]), 10),
    (dict(grid=[[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 0, 0]]), 10),
    (dict(grid=[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 0, 0, 1, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]), 8),
    (dict(grid=[[1, 0, 1], [1, 1, 1]]), 5),
    (dict(grid=[[1, 0, 1, 0], [0, 1, 0, 1]]), 5),
]

s = Solution()
for e, a in examples:
    print(a, e)
    print(s.minimumSum(**e))
