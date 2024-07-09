# 924 尽量减少恶意软件的传播
# https://leetcode.cn/problems/minimize-malware-spread/


# leetcode submit region begin(Prohibit modification and deletion)
# 超时
# class Solution:
#     def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
#         n = len(graph)
#         for k in range(n):
#             for i in range(n):
#                 for j in range(n):
#                     if i != j:
#                         graph[i][j] |= graph[i][k] and graph[k][j]
#                         graph[j][i] = graph[i][j]
#         initial = set(initial)
#         return \
#             sorted(
#                 [(sum(graph[i]), i) for i in initial if len(set([j for j in range(n) if graph[i][j]]) & initial) == 1] +
#                 [(-1, min(initial))],
#                 key=lambda x: (-x[0], x[1]))[0][1]


class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        n = len(graph)
        p = [i for i in range(n)]
        size = [1] * n

        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        for i in range(n):
            for j in range(i + 1, n):
                if graph[i][j] == 1:
                    pi, pj = find(i), find(j)
                    # print(i, j, pi, pj, p)
                    if pi != pj:
                        if size[pi] < size[pj]:
                            p[pi] = pj
                            size[pj] += size[pi]
                        else:
                            p[pj] = pi
                            size[pi] += size[pj]
        cnt = Counter(find(x) for x in initial)
        a = [(-1, min(initial))]
        for x in initial:
            o = find(x)
            if cnt[o] == 1:
                a.append((size[o], x))
        return sorted(a, key=lambda x: (-x[0], x[1]))[0][1]


"""
class UnionFind:
    __slots__ = "p", "size"

    def __init__(self, n: int):
        self.p = list(range(n))
        self.size = [1] * n

    def find(self, x: int) -> int:
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, a: int, b: int) -> bool:
        pa, pb = self.find(a), self.find(b)
        if pa == pb:
            return False
        if self.size[pa] > self.size[pb]:
            self.p[pb] = pa
            self.size[pa] += self.size[pb]
        else:
            self.p[pa] = pb
            self.size[pb] += self.size[pa]
        return True

    def get_size(self, root: int) -> int:
        return self.size[root]


class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        n = len(graph)
        uf = UnionFind(n)
        for i in range(n):
            for j in range(i + 1, n):
                graph[i][j] and uf.union(i, j)
        cnt = Counter(uf.find(x) for x in initial)
        print(*graph, sep="\n")
        print(uf.size)
        print(uf.p)
        print()
        ans, mx = n, 0
        for x in initial:
            root = uf.find(x)
            if cnt[root] > 1:
                continue
            sz = uf.get_size(root)
            if sz > mx or (sz == mx and x < ans):
                ans = x
                mx = sz
        return min(initial) if ans == n else ans
"""

# DFS
# class Solution:
#     def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
#         def dfs(i: int, o: int):
#             vis[i] = True
#             nums[o] += 1
#             infect[o] += i in initial
#             root[i] = o
#             for j in range(n):
#                 if graph[i][j] == 1 and not vis[j]:
#                     dfs(j, o)
#
#         n = len(graph)
#         initial = set(initial)
#         vis = [False] * n
#         root = [-1] * n
#         infect = [0] * n
#         nums = [0] * n
#         for i in range(n):
#             if not vis[i]:
#                 dfs(i, i)
#         ans = min(initial)
#         mx = 0
#         for i in initial:
#             o = root[i]  # 节点 i 所在的连通块的编号
#             if infect[o] == 1:  # 这个连通块只有一个受感染
#                 if mx < nums[o]:  # 更新能减少感染的数量和节点索引
#                     mx = nums[o]
#                     ans = i
#                 elif mx == nums[0]:
#                     ans = min(ans, i)
#         return ans

# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
a = s.minMalwareSpread([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [2, 1])
# a = s.minMalwareSpread([[1, 1, 0], [1, 1, 0], [0, 0, 1]], [0, 1])
