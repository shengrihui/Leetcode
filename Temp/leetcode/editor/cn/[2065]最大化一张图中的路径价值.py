# 2065 最大化一张图中的路径价值
# https://leetcode.cn/problems/maximum-path-quality-of-a-graph/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        def dfs(x: int, sum_time: int, sum_value: int) -> int:
            if x == 0:
                nonlocal ans
                if sum_value > ans:
                    ans = sum_value
                # 不 return
            for y, t in g[x]:
                if t + sum_time > maxTime:
                    continue
                if not vis[y]:
                    vis[y] = True
                    dfs(y, sum_time + t, sum_value + values[y])
                    vis[y] = False
                else:  # 回到已经访问过的节点，value 就不加了
                    dfs(y, sum_time + t, sum_value)

        n = len(values)
        g = [[] for _ in range(n)]
        for u, v, t in edges:
            g[u].append((v, t))
            g[v].append((u, t))
        vis = [False] * n
        vis[0] = True
        ans = 0
        dfs(0, 0, values[0])
        return ans

# leetcode submit region end(Prohibit modification and deletion)
