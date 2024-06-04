# 3067 在带权树网络中统计可连接服务器对数目
# https://leetcode.cn/problems/count-pairs-of-connectable-servers-in-a-weighted-tree-network/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        n = len(edges) + 1
        g = [[] for _ in range(n)]
        for a, b, w in edges:
            g[a].append((b, w))
            g[b].append((a, w))

        def dfs(fa: int, x: int, w: int):
            nonlocal c
            c += w % signalSpeed == 0
            for son, weight in g[x]:
                if son == fa:
                    continue
                dfs(x, son, w + weight)

        ans = [0] * n
        for root in range(n):
            cnt_s = 0
            for son, w in g[root]:
                c = 0
                dfs(root, son, w)
                ans[root] += cnt_s * c
                cnt_s += c
        return ans

# leetcode submit region end(Prohibit modification and deletion)
