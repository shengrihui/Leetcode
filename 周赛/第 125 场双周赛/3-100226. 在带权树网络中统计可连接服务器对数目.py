# 第 125 场双周赛 第 3 题
# 题目：100226. 在带权树网络中统计可连接服务器对数目
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-125/problems/count-pairs-of-connectable-servers-in-a-weighted-tree-network/
# 题库：https://leetcode.cn/problems/count-pairs-of-connectable-servers-in-a-weighted-tree-network

from typing import List
from collections import *
from itertools import *
from functools import *
from math import inf, gcd, sqrt, isqrt
import bisect
from bisect import *

# 超时
"""
class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        n = len(edges) + 1
        g = [[inf] * n for _ in range(n)]
        t = [[] for _ in range(n)]
        for a, b, w in edges:
            g[a][b] = g[b][a] = w
            t[a].append(b)
            t[b].append(a)
        ans = [0] * n
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if i == j or i == k or j == k: continue
                    g[i][j] = min(g[i][j], g[i][k] + g[k][j])
        for i in range(n):
            for j in range(n):
                if g[i][j] % signalSpeed == 0:
                    g[i][j] = g[j][i] = 0

        @cache
        def dfs(x: int, fa: int, root: int) -> int:
            res = g[root][x] == 0
            for y in t[x]:
                if y == fa:
                    continue
                res += dfs(y, x, root)
            # print(x,fa,root,res)
            return res

        for root in range(n):
            s = 0
            for son in t[root]:
                tmp = dfs(son, root, root)
                ans[root] += s * tmp
                s += tmp
        # print(*g,sep="\n")
        return ans
"""


class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        n = len(edges) + 1
        g = [[] for _ in range(n)]
        for a, b, w in edges:
            g[a].append((b, w))
            g[b].append((a, w))



s = Solution()
examples = [
    (dict(edges=[[0, 1, 1], [1, 2, 5], [2, 3, 13], [3, 4, 9], [4, 5, 2]], signalSpeed=1), [0, 4, 6, 6, 4, 0]),
    (dict(edges=[[0, 6, 3], [6, 5, 3], [0, 3, 1], [3, 2, 7], [3, 1, 6], [3, 4, 2]], signalSpeed=3),
     [2, 0, 0, 0, 0, 0, 2]),
]
for e, a in examples:
    print(a, e)
    print(s.countPairsOfConnectableServers(**e))
