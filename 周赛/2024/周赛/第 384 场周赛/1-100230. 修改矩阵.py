# 第 384 场周赛 第 1 题
# 题目：100230. 修改矩阵
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-384/problems/modify-the-matrix/
# 题库：https://leetcode.cn/problems/modify-the-matrix

from typing import List
from collections import *
from itertools import *
from functools import *
from math import inf, gcd, sqrt, isqrt
import bisect
from bisect import *


class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        mx = [max(col) for col in zip(*matrix)]
        return [[mx[j] if x == -1 else x for j, x in enumerate(row)] for i, row in enumerate(matrix)]


s = Solution()
examples = [
    (dict(matrix=[[1, 2, -1], [4, -1, 6], [7, 8, 9]]), [[1, 2, 9], [4, 8, 6], [7, 8, 9]]),
    (dict(matrix=[[3, -1], [5, 2]]), [[3, 2], [5, 2]]),
]
for e, a in examples:
    print(a, e)
    print(s.modifiedMatrix(**e))
