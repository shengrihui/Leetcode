# 第 406 场周赛 第 3 题
# 题目：100361. 切蛋糕的最小总开销 I
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-406/problems/minimum-cost-for-cutting-cake-i/
# 题库：https://leetcode.cn/problems/minimum-cost-for-cutting-cake-i

from functools import *
from math import inf
from typing import List


class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        @cache
        def dfs(up: int, down: int, left: int, right: int) -> int:
            # print(up, down, left, right)
            if up == down - 1 and left == right - 1:
                return 0
            res = inf
            for i in range(up + 1, down):
                res = min(res, horizontalCut[i] + dfs(up, i, left, right) + dfs(i, down, left, right))
            for j in range(left + 1, right):
                res = min(res, verticalCut[j] + dfs(up, down, left, j) + dfs(up, down, j, right))
            return res

        horizontalCut = [0] + horizontalCut + [0]
        verticalCut = [0] + verticalCut + [0]
        return dfs(0, m + 1, 0, n + 1)


s = Solution()
examples = [
    (dict(m=3, n=2, horizontalCut=[1, 3], verticalCut=[5]), 13),
    (dict(m=2, n=2, horizontalCut=[7], verticalCut=[4]), 15),
]
for e, a in examples:
    print(a, e)
    print(s.minimumCost(**e))
