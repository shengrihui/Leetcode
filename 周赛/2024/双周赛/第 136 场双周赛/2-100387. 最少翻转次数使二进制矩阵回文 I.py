# 第 136 场双周赛 第 2 题
# 题目：100387. 最少翻转次数使二进制矩阵回文 I
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-136/problems/minimum-number-of-flips-to-make-binary-grid-palindromic-i/
# 题库：https://leetcode.cn/problems/minimum-number-of-flips-to-make-binary-grid-palindromic-i

from typing import List


class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        res1 = 0
        for i, row in enumerate(grid):
            for j in range(m // 2):
                res1 += row[j] != row[-1 - j]
        res2 = 0
        for j, col in enumerate(zip(*grid)):
            for i in range(n // 2):
                res2 += col[i] != col[-1 - i]
        return min(res1, res2)


s = Solution()
examples = [
    (dict(grid=[[1, 0, 0], [0, 0, 0], [0, 0, 1]]), 2),
    (dict(grid=[[0, 1], [0, 1], [0, 0]]), 1),
    (dict(grid=[[1], [0]]), 0),
]
for e, a in examples:
    print(a, e)
    print(s.minFlips(**e))
