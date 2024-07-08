# 题目：100158. 转换字符串的最小成本 II
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-377/problems/minimum-cost-to-convert-string-ii/
# 题库：https://leetcode.cn/problems/minimum-cost-to-convert-string-ii
from collections import defaultdict
from heapq import *
from math import inf
from typing import List


# Dijkstra + DP
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # 建图
        path = defaultdict(dict)
        for o, ch, c in zip(original, changed, cost):
            if ch not in path[o]:
                path[o][ch] = c
            elif c < path[o][ch]:
                path[o][ch] = c

        # 要求 x 到其他所有点的最短距离，所以用 dijkstra
        dist = dict()
        for x in path:
            dist[x] = dict()
            dist[x][x] = 0
            h = [(0, x)]  # 先将 x->x 到自己为 0 的入堆
            while h:
                d, u = heappop(h)  # 弹出堆顶: x 到 u 的距离 d
                # x 到 u 的最短距离确实是 d 
                # 并且 u 可以作为出发（u 没有到头，x 到 path[u] 的点可以连接）
                if dist[x][u] == d and u in path:
                    for v in path[u]:
                        # v 还没有访问过 or x 到 v 可以更短
                        if v not in dist[x] or dist[x][v] > d + path[u][v]:
                            dist[x][v] = d + path[u][v]
                            heappush(h, (dist[x][v], v))

        n = len(source)
        dp = [inf] * (n + 1)
        dp[0] = 0
        for i in range(n):
            if source[i] == target[i]:
                dp[i + 1] = dp[i]
            vis = set()
            for from_ in dist:
                len_f = len(from_)
                # 这一长度没有被记录过，source[:i] 有足够长
                if len_f not in vis and i + 1 >= len_f:
                    s = source[i - len_f + 1:i + 1]
                    to = target[i - len_f + 1:i + 1]
                    # source 前的这一段可以改变成 to
                    if s == from_ and to in dist[from_]:
                        dp[i + 1] = min(dp[i + 1], dp[i - len_f + 1] + dist[from_][to])
                        vis.add(len_f)

        return dp[n] if dp[n] != inf else -1


s = Solution()
examples = [
    (dict(source="abcd", target="acbe", original=["a", "b", "c", "c", "e", "d"], changed=["b", "c", "b", "e", "b", "e"],
          cost=[2, 5, 5, 1, 2, 20]), 28),
    (dict(source="abcdefgh", target="acdeeghh", original=["bcd", "fgh", "thh"], changed=["cde", "thh", "ghh"],
          cost=[1, 3, 5]), 9),
    (dict(source="abcdefgh", target="addddddd", original=["bcd", "defgh"], changed=["ddd", "ddddd"], cost=[100, 1578]),
     -1),
    (dict(source="a", target="d", original=["a"], changed=["b"], cost=[1]),
     -1),
]
for e, a in examples:
    print(a, e)
    print(s.minimumCost(**e))
