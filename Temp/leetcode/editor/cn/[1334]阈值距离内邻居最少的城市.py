# 1334 阈值距离内邻居最少的城市
from math import *
from typing import *


# class Solution:
#     def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
#         mp = [[0] * n for _ in range(n)]
#         for f, t, d in edges:
#             mp[f][t] = mp[t][f] = d
#
#         def dfs(start, now, dist):
#             nonlocal vis, ans
#             for son in range(n):
#                 if not vis[son] and (d := mp[now][son]):
#                     if (dd := dist + d) <= distanceThreshold:
#                         vis[son] = True
#                         ans[start].add(son)
#                         dfs(start, son, dd)
#                         vis[son] = False
#
#         ans = [set() for _ in range(n)]
#         for start in range(n):
#             vis = [False] * n
#             vis[start] = True
#             dfs(start, start, 0)
#         ans = sorted(enumerate(ans), key=lambda x: (len(x[1]), -x[0]))
#         return ans[0][0]

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        mp = [[inf] * n for _ in range(n)]
        for f, t, d in edges:
            mp[f][t] = mp[t][f] = d

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if (d := mp[i][k] + mp[k][j]) < mp[i][j]:
                        mp[i][j] = d
        cnt = [sum(mp[i][j] <= distanceThreshold for j in range(n) if j != i) for i in range(n)]
        ans = sorted(enumerate(cnt), key=lambda x: (x[1], -x[0]))
        return ans[0][0]

# leetcode submit region end(Prohibit modification and deletion)
