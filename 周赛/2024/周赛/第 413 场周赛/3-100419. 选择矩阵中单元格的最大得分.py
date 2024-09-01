# 第 413 场周赛 第 3 题
# 题目：100419. 选择矩阵中单元格的最大得分
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-413/problems/select-cells-in-grid-with-maximum-score/
# 题库：https://leetcode.cn/problems/select-cells-in-grid-with-maximum-score

from collections import *
from functools import *
from typing import List

"""
题目要选一些不同数字且来自不同的行


值的范围是 [1,100]，用二进制表示哪些数字选过了就太大了
但最多就 10 行，用二进制表示哪些行选了的状态就 1023 个

构造 d[x] = [...] 为 x 这个值在哪些行里有

dfs(i,mask) 现在考虑第 i 个数字，之前已经选的行是 mask 所代表的二进制集合
第 i 个数要么选，要么选一个之前没选过的那一行
递归入口：dfs(0,0)
递归出口：
    1. 选完了所有数字（假如好大的 grid 但是只有一两种数字）
    2. 选够了 mask.bit_count() == len(grid) 个数字
"""


class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        @cache
        def dfs(i: int, mask: int) -> int:
            if mask.bit_count() == len(grid) or i == len(a):
                return 0
            res = dfs(i + 1, mask)
            x = a[i][0]
            for j, ii in enumerate(a[i][1]):
                if mask >> ii & 1 == 0:
                    r = dfs(i + 1, mask | 1 << ii) + x
                    if r > res:
                        res = r
            return res

        d = defaultdict(list)
        for i, row in enumerate(grid):
            for x in set(row):
                d[x].append(i)
        a = list(d.items())
        return dfs(0, 0)


s = Solution()
examples = [
    (dict(grid=[[1, 2, 3], [4, 3, 2], [1, 1, 1]]), 8),
    (dict(grid=[[5, 5], [5, 5], [11, 5]]), 16),
    (dict(grid=[[8, 7, 6], [8, 3, 2]]), 15),
]
for e, a in examples:
    print(a, e)
    print(s.maxScore(**e))
