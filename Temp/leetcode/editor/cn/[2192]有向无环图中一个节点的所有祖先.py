# 2192 有向无环图中一个节点的所有祖先
# https://leetcode.cn/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ans = [set() for _ in range(n)]
        indeg = [0] * n
        g = [[] for _ in range(n)]
        for f, t in edges:
            g[f].append(t)
            indeg[t] += 1
        # BFS 拓扑排序
        q = deque(i for i in range(n) if indeg[i] == 0)
        while q:
            node = q.popleft()
            for son in g[node]:
                ans[son].add(node)
                ans[son].update(ans[node])
                indeg[son] -= 1
                if indeg[son] == 0:
                    q.append(son)
        return [sorted(t) for t in ans]


# 超时
"""
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        g = [[False] * n for _ in range(n)]
        for f, t in edges:
            g[t][f] = True
        for k in range(n):
            for j in range(n):
                for i in range(n):
                    g[j][i] |= g[j][k] and g[k][i]
        ans = []
        for t in range(n):
            t = [f for f in range(n) if g[t][f]]
            ans.append(sorted(t))
        return ans
"""
# leetcode submit region end(Prohibit modification and deletion)
