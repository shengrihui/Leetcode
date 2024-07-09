# 310 最小高度树
# https://leetcode.cn/problems/minimum-height-trees/

# leetcode submit region begin(Prohibit modification and deletion)

# BFS / DFS
# 以 0 为开始找离 0 最远的 x
# 以 x 为开始找离 x 最远的 y
# (x,y) 是最远的两个节点
# 　x 找 y 的过程中，记录每一个节点的父节点
# 最后从 y 往沿着父节点回找 x 构造路径
# BFS ，0 -> x 的时候，parent[x] 会变
# x -> y 的时候，parent[x] 不是 -1
# 所以要将 parent[x] = -1
# 而在 dfs 中，
# x -> y 的过程中，parent[x] 已经设置为 -1 了
"""
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        g = [[] for _ in range(n)]
        parent = [-1] * n  #
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        def bfs(start: int) -> int:
            vis = [False] * n
            q = deque([start])
            vis[start] = True
            while q:
                x = q.popleft()
                for y in g[x]:
                    if not vis[y]:
                        q.append(y)
                        vis[y] = True
                        parent[y] = x
            return x  # 返回 x ，队列装的最后一个

        # 距离最远的两个点
        x = bfs(0)
        y = bfs(x)
        parent[x] = -1
        path = []
        # 这竟然有点链表的感觉
        while y != -1:
            path.append(y)
            y = parent[y]
        m = len(path)
        return [path[m // 2]] if m % 2 else [path[m // 2], path[m // 2 - 1]]
"""
# DFS
"""
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        g = [[] for _ in range(n)]
        parent = [-1] * n  #
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        max_depth, node = 0, -1

        def dfs(x: int, fa: int, depth: int) -> None:
            nonlocal max_depth, node
            if depth > max_depth:
                node, max_depth = x, depth
            parent[x] = fa
            for son in g[x]:
                if son != fa:
                    dfs(son, x, depth + 1)

        dfs(0, -1, 0)
        max_depth = 0
        dfs(node, -1, 0)
        path = []
        while node != -1:
            path.append(node)
            node = parent[node]
        m = len(path)
        return [path[m // 2]] if m % 2 else [path[m // 2], path[m // 2 - 1]]
"""


# 拓扑排序
# 叶子节点向里包围，直到剩余节点 <= 2
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        g = [[] for _ in range(n)]
        deg = [0] * n
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
            deg[a] += 1
            deg[b] += 1
        q = [i for i, d in enumerate(deg) if d == 1]
        remainNodes = n
        vis = set(q)
        while remainNodes > 2:
            tmp = q
            q = []
            remainNodes -= len(tmp)
            for i in tmp:
                for j in g[i]:
                    if j not in vis:
                        deg[j] -= 1
                        if deg[j] == 1:
                            q.append(j)
        return q

# leetcode submit region end(Prohibit modification and deletion)
