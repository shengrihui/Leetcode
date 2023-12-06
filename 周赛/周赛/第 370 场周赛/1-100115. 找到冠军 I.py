from typing import List
from collections import *
from itertools import *
from functools import *
from math import *


# 题目：100115. 找到冠军 I
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-370/problems/find-champion-i/
# 题库：

class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n = len(grid)
        for i, a in enumerate(grid):
            if sum(a) == n - 1:
                return i


s = Solution()
examples = [
    (dict(grid=[[0, 1], [0, 0]]), 0),
    (dict(grid=[[0, 0, 1], [1, 0, 1], [0, 0, 0]]), 1),
]
for e, a in examples:
    print(a, e)
    print(s.findChampion(**e))
