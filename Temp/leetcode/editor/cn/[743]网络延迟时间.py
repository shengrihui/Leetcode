# 743 网络延迟时间
# https://leetcode.cn/problems/network-delay-time/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dis = [inf] * (n + 1)
        dis[0] = dis[k] = 0
        g = [[] for _ in range(n + 1)]
        q = deque()
        for u, v, w in times:
            g[u].append((v, w))
            if u == k:
                q.append((u, v, w))
        while q:
            u, v, w = q.popleft()
            if dis[v] <= dis[u] + w:
                continue
            dis[v] = dis[u] + w
            for nv, nw in g[v]:
                if nw + dis[v] >= dis[nv]:
                    continue
                q.append((v, nv, nw))
        ans = max(dis)
        return -1 if ans == inf else ans

# leetcode submit region end(Prohibit modification and deletion)
