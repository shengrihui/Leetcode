# 2101 引爆最多的炸弹
# https://leetcode.cn/problems/detonate-the-maximum-bombs/
# from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
"""
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        g = [[0] * n for _ in range(n)]
        for i, (x, y, r) in enumerate(bombs):
            for j in range(i + 1, n):
                xx, yy, rr = bombs[j]
                d = (x - xx) ** 2 + (y - yy) ** 2
                g[i][j] = g[j][i] = d
        ans = 0
        for i in range(n):
            q = deque([i])
            vis = {i}
            while q:
                x = q.popleft()
                r = bombs[x][2] ** 2
                for y, d in enumerate(g[x]):
                    if y not in vis and r >= d:
                        q.append(y)
                        vis.add(y)
            ans = max(ans, len(vis))
        return ans
"""
import math


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        g = [[] for _ in range(n)]
        for i, (x, y, r) in enumerate(bombs):
            for j in range(i + 1, n):
                xx, yy, rr = bombs[j]
                d = math.hypot(x - xx, y - yy)
                if d <= r: g[i].append(j)
                if d <= rr: g[j].append(i)
        ans = 0
        for i in range(n):
            q = deque([i])
            vis = {i}
            while q:
                x = q.popleft()
                for y in g[x]:
                    if y not in vis:
                        q.append(y)
                        vis.add(y)
            if len(vis) > ans:
                ans = len(vis)
                if ans == n:
                    break
        return ans


# 灵神 bitset + Floyd
"""
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        f = [0] * n
        for i, (x, y, r) in enumerate(bombs):
            for j, (x2, y2, _) in enumerate(bombs):
                dx = x - x2
                dy = y - y2
                if dx * dx + dy * dy <= r * r:
                    f[i] |= 1 << j  # i 可以到达 j

        for k in range(n):
            for i in range(n):
                if f[i] >> k & 1:  # i 可以到达 k
                    f[i] |= f[k]  # i 也可以到 k 可以到达的点

        return max(s.bit_count() for s in f)  # 集合大小的最大值
"""
# leetcode submit region end(Prohibit modification and deletion)E:\CS\Algorithm\Leetcode\Temp\leetcode\editor\cn\[2101]引爆最多的.py
