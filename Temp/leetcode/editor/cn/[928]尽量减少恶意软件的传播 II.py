# 928 尽量减少恶意软件的传播 II
# https://leetcode.cn/problems/minimize-malware-spread-ii/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)

# 并查集
class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        def find(x: int) -> int:
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        n = len(graph)
        p = list(range(n))
        st = set(initial)
        # 能感染当前联通分量的节点编号，含义与 DFS 相同
        node_id = [-1] * n
        size = [1] * n
        for x, row in enumerate(graph):
            for y, conn in enumerate(row):
                if conn == 0 or y <= x or y in st and x in st:
                    continue
                px, py = find(x), find(y)
                if x in st:
                    node_id[py] = x if node_id[py] == -1 else -2
                    continue
                if y in st:
                    node_id[px] = y if node_id[px] == -1 else -2
                    continue
                if px != py:
                    if size[px] < size[py]:
                        # 往 x 合并，往大的合并
                        px, py = py, px
                    p[py] = px
                    size[px] += size[py]
                    if node_id[py] != node_id[px]:  # 两个相同就不用考虑了，该是啥就是啥
                        if node_id[px] == -1:
                            node_id[px] = node_id[py]
                        elif node_id[py] != -1:  # 两个都不是 -1，且两个不一样，那么合并之后就有两个感染节点可以感染她们
                            node_id[py] = -2

        cnt = Counter()
        add = set()
        for i in range(n):
            o = find(i)
            # i 所在的连通块只被一个感染节点感染
            # 并且该连通块还没统计过
            if node_id[o] >= 0 and o not in add:
                cnt[node_id[o]] += size[o]
                add.add(o)
        return min((-size, node_id) for node_id, size in cnt.items())[1] if cnt else min(initial)


# DFS
"""
class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        def dfs(x: int) -> None:
            vis[x] = True
            nonlocal node_id, size
            size += 1  # 下面的 elif not vis[y]: 保证 x 是没有被感染的
            for y, conn in enumerate(graph[x]):
                if conn == 0:
                    continue
                if y in st:  # y 是被感染的
                    if node_id == -1:  # 第一次遇到感染点
                        node_id = y
                    elif node_id >= 0 and node_id != y:  # 遇到第二个感染点
                        node_id = -2
                elif not vis[y]:
                    # y 是没有被感染的并且还没有被访问过
                    dfs(y)

        st = set(initial)
        n = len(graph)
        vis = [False] * n
        cnt = Counter()
        for i, seen in enumerate(vis):
            if seen or i in st:  # 访问过的节点或者已经被感染的节点 continue
                continue
            # 当前连通块会被 node_id 节点感染
            # node_id = -1，不会被感染
            # node_id = -2，会被多个节点感染，也就是最终会会感染
            node_id = -1
            size = 0  # 当前连通块大小
            dfs(i)
            if node_id >= 0:
                # 删掉 node_id 后免于感染的数量
                cnt[node_id] += size
        return min((-size, node_id) for node_id, size in cnt.items())[1] if cnt else min(initial)
"""
# leetcode submit region end(Prohibit modification and deletion)
"""
[[1,1,0,0,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0],[0,0,0,1,0,0,1,0,0,1],[0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0],[0,0,0,1,0,0,1,0,0,0],[0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,0,1,0],[0,0,0,1,0,0,0,0,0,1]]
[2,1,9]

"""
