# 2316 统计无向图中无法互相到达点对数
from collections import *
from typing import *


# class Solution:
#     def countPairs(self, n: int, edges: List[List[int]]) -> int:
#         mp = [[False] * n for _ in range(n)]
#         for a, b in edges:
#             mp[a][b] = True
#             mp[b][a] = True
#         for k in range(n):
#             for i in range(n):
#                 for j in range(n):
#                     mp[i][j] |= mp[i][k] and mp[k][j]
#                     mp[j][i] = mp[i][j]
#         ans = 0
#         for i in range(n):
#             for j in range(i):
#                 ans += not mp[i][j]
#         return ans

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        mp = [[] for _ in range(n)]
        for a, b in edges:
            mp[a].append(b)
            mp[b].append(a)
        a = []
        vis = [False] * n

        def bfs(s):
            nonlocal vis
            cnt = 1
            q = deque()
            q.append(s)
            vis[s] = True
            while q:
                m = q.popleft()
                for i in mp[m]:
                    if not vis[i]:
                        q.append(i)
                        vis[i] = True
                        cnt += 1
            return cnt

        ans = 0
        for i in range(n):
            if not vis[i]:
                c = bfs(i)
                ans += c * (n - c)
        return ans // 2

    # leetcode submit region end(Prohibit modification and deletion)
