from typing import List
from collections import *
from itertools import *
from functools import *
from math import *


# 题目：100138. 最大化网格图中正方形空洞的面积
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-118/problems/maximize-area-of-square-hole-in-grid/
# 题库：https://leetcode.cn/problems/maximize-area-of-square-hole-in-grid

class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        def helper(a: int, bar: List[int]) -> int:
            bar.sort()
            mx = 0
            i = 0
            l = 1
            while i < len(bar):
                while i < len(bar) - 1 and bar[i] + 1 == bar[i + 1]:
                    i += 1
                    l += 1
                mx = max(mx, l + 1)
                l = 1
                i += 1
            return mx

        h = helper(n, hBars)
        v = helper(m, vBars)

        return min(h, v) ** 2


s = Solution()
examples = [
    (dict(n=2, m=1, hBars=[2, 3], vBars=[2]), 4),
    (dict(n=1, m=1, hBars=[2], vBars=[2]), 4),
    (dict(n=2, m=3, hBars=[2, 3], vBars=[2, 3, 4]), 9),
    (dict(n=2, m=4, hBars=[2, 3], vBars=[2,  4]), 4),
]
for e, a in examples:
    print(a, e)
    print(s.maximizeSquareHoleArea(**e))
