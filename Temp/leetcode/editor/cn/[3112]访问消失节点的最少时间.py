# 3112 访问消失节点的最少时间
# https://leetcode.cn/problems/minimum-time-to-visit-disappearing-nodes/
from imports import *

# leetcode submit region begin(Prohibit modification and deletion)
#	执行耗时:650 ms,击败了6.82% 的Python3用户
#   内存消耗:69.2 MB,击败了16.73% 的Python3用户
"""
class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        g = [defaultdict(lambda: inf) for _ in range(n)]
        for u, v, l in edges:
            g[u][v] = g[v][u] = min(g[u][v], l)
        dist = [inf] * n
        dist[0] = 0
        q = [[0, 0]]
        while q:
            u, dis = heappop(q)
            if dis > dist[u]:
                continue
            for v, d in g[u].items():
                nd = dis + d
                if nd < disappear[v] and nd < dist[v]:
                    dist[v] = dis + d
                    heappush(q,[v, dis + d])
        return [d if d != inf  else -1 for i, d in enumerate(dist)]
"""
# 双端队列
#	执行耗时:381 ms,击败了30.76% 的Python3用户
#	内存消耗:69.3 MB,击败了16.73% 的Python3用户
"""
class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        g = [defaultdict(lambda: inf) for _ in range(n)]
        for u, v, l in edges:
            g[u][v] = g[v][u] = min(g[u][v], l)
        dist = [inf] * n
        dist[0] = 0
        q = deque([[0, 0]])
        while q:
            u, dis = q.popleft()
            if dis > dist[u]:
                continue
            for v, d in g[u].items():
                nd = dis + d
                if nd < disappear[v] and nd < dist[v]:
                    dist[v] = dis + d
                    q.append([v, dis + d])
        return [d if d != inf  else -1 for i, d in enumerate(dist)]
"""


# 灵神的改成队列
#	执行耗时:274 ms,击败了63.96% 的Python3用户
#	内存消耗:65.8 MB,击败了38.35% 的Python3用户
class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        g = [[] for _ in range(n)]  # 稀疏图用邻接表
        for x, y, wt in edges:
            g[x].append((y, wt))
            g[y].append((x, wt))

        dis = [-1] * n
        dis[0] = 0
        h = deque([(0, 0)])
        while h:
            dx, x = h.popleft()
            if dx > dis[x]:  # x 之前出堆过
                continue
            for y, wt in g[x]:
                new_dis = dx + wt
                if new_dis < disappear[y] and (dis[y] < 0 or new_dis < dis[y]):
                    dis[y] = new_dis  # 更新 x 的邻居的最短路
                    h.append((new_dis, y))
        return dis
# leetcode submit region end(Prohibit modification and deletion)
