from collections import *
from typing import List


# 题目：# 8051. 可以被 K 整除连通块的最大数目
# 题目链接：
# https://leetcode.cn/contest/biweekly-contest-114/problems/maximum-number-of-k-divisible-components/
class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        q = deque(i for i in range(n) if len(g[i]) == 1)


s = Solution()
examples = [
    (dict(n=5, edges=[[0, 2], [1, 2], [1, 3], [2, 4]], values=[1, 8, 1, 4, 4], k=6), 2),
    (dict(n=7, edges=[[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]], values=[3, 0, 6, 1, 5, 2, 1], k=3), 3),
]
for e, a in examples:
    print(a, e)
    print(s.maxKDivisibleComponents(**e))
