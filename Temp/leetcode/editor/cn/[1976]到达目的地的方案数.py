# 1976 到达目的地的方案数
# https://leetcode.cn/problems/number-of-ways-to-arrive-at-destination/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        e = [[] for _ in range(n)]
        for u, v, t in roads:
            e[u].append((v, t))
            e[v].append((u, t))
        times = [0] + [inf] * (n - 1)  # 路口 0 到其他路口的最少时间
        ways = [1] + [0] * (n - 1)  # 路口 0 到其他路口最少时间的方案数

        q = [(0, 0)]  # 按照排序方式，（时间，路口编号）
        while q:
            time, u = heappop(q)
            if time > times[u]:  # 如果到 u 的时间比最少时间大
                continue
            for v, t in e[u]:
                nt = time + t  # 到 v 的新时间
                if nt < times[v]:  # 更新到 v 的时间
                    times[v] = nt
                    ways[v] = ways[u]
                    heappush(q, (nt, v))
                elif nt == times[v]:  # 方案数加 1
                    ways[v] = (ways[v] + ways[u]) % MOD
        return ways[-1]

# leetcode submit region end(Prohibit modification and deletion)
