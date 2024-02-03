from typing import List
from collections import *
from itertools import *
from functools import *
from math import inf, gcd


# 题目：100188. 按距离统计房屋对数目 I
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-381/problems/count-the-number-of-houses-at-a-certain-distance-i/
# 题库：https://leetcode.cn/problems/count-the-number-of-houses-at-a-certain-distance-i

class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        g = [[n + 4] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                g[i][j] = g[j][i] = abs(i - j)
        if x != y:
            g[x - 1][y - 1] = g[y - 1][x - 1] = 1
        for k in [x - 1, y - 1]:
            for i in range(n):
                for j in range(n):
                    g[i][j] = min(g[i][j], g[i][k] + g[k][j])

        res = [0] * n
        for a in range(1, n):
            s = 0
            for i in range(n):
                for j in range(n):
                    s += a == g[i][j]
            res[a - 1] = s
        return res


s = Solution()
examples = [
    (dict(n=3, x=1, y=3), [6, 0, 0]),
    (dict(n=5, x=2, y=4), [10, 8, 2, 0, 0]),
    (dict(n=4, x=1, y=1), [6, 4, 2, 0]),
]
for e, a in examples:
    print(a, e)
    print(s.countOfPairs(**e))
