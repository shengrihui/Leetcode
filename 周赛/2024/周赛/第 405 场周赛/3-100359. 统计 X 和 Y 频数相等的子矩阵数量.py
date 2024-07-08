# 第 405 场周赛 第 3 题
# 题目：100359. 统计 X 和 Y 频数相等的子矩阵数量
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-405/problems/count-submatrices-with-equal-frequency-of-x-and-y/
# 题库：https://leetcode.cn/problems/count-submatrices-with-equal-frequency-of-x-and-y

from typing import List


class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        x = [[0] * (m + 1) for _ in range(n + 1)]
        y = [[0] * (m + 1) for _ in range(n + 1)]
        ans = 0
        for i, row in enumerate(grid):
            for j, c in enumerate(row):
                x[i + 1][j + 1] = x[i + 1][j] + x[i][j + 1] - x[i][j] + (c == "X")
                y[i + 1][j + 1] = y[i + 1][j] + y[i][j + 1] - y[i][j] + (c == "Y")
                if x[i + 1][j + 1] > 0 and x[i + 1][j + 1] == y[i + 1][j + 1]:
                    ans += 1
        return ans


# O(n) 空间
class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        ans = 0
        col_cnt = [[0, 0] for _ in grid[0]]  # 第 i 列 x y 的个数
        for row in grid:
            sx, sy = 0, 0  # (0,0) 到 (i,j) 的 x y 的个数
            for j, c in enumerate(row):
                if c == "X":
                    col_cnt[j][0] += 1
                elif c == "Y":
                    col_cnt[j][1] += 1
                sx += col_cnt[j][0]
                sy += col_cnt[j][1]
                if sx > 0 and sx == sy:
                    ans += 1
        return ans


s = Solution()
examples = [
    (dict(grid=[["X", "Y", "."], ["Y", ".", "."]]), 3),
    (dict(grid=[["X", "X"], ["X", "Y"]]), 0),
    (dict(grid=[[".", "."], [".", "."]]), 0),
]
for e, a in examples:
    print(a, e)
    print(s.numberOfSubmatrices(**e))
