# 第 392 场周赛 第 4 题
# 题目：100244. 带权图里旅途的最小代价
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-392/problems/minimum-cost-walk-in-weighted-graph/
# 题库：https://leetcode.cn/problems/minimum-cost-walk-in-weighted-graph

from typing import List


class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n
        self.weights = [-1] * n
        self.n = n
        # 当前连通分量数目
        self.setCount = n

    def findset(self, x: int) -> int:
        if self.parent[x] == x:
            return x
        self.parent[x] = self.findset(self.parent[x])
        return self.parent[x]

    def unite(self, x: int, y: int, w: int) -> bool:
        # print(x,y)
        x, y = self.findset(x), self.findset(y)
        # if x == y:
        #     return False
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]
        self.weights[x] &= w & self.weights[y]
        self.setCount -= 1
        return True

    def connected(self, x: int, y: int) -> bool:
        x, y = self.findset(x), self.findset(y)
        return x == y


class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        u = UnionFind(n)
        for x, y, w in edges:
            u.unite(x, y, w)
        ans = []
        for s, t in query:
            if s == t:
                ans.append(0)
            elif u.connected(s, t):
                ans.append(u.weights[u.findset(t)])
            else:
                ans.append(-1)
        return ans


s = Solution()
examples = [
    (dict(n=9, edges=[[0, 4, 7], [3, 5, 1], [1, 3, 5], [1, 5, 1]], query=
    [[0, 4], [1, 5], [3, 0], [3, 3], [3, 2], [2, 0], [7, 7], [7, 0]]), [7, 1, -1, 0, -1, -1, 0, -1]),
    (dict(n=5, edges=[[0, 1, 7], [1, 3, 7], [1, 2, 1]], query=[[0, 3], [3, 4]]), [1, -1]),
    (dict(n=3, edges=[[0, 2, 7], [0, 1, 15], [1, 2, 6], [1, 2, 1]], query=[[1, 2]]), [0]),
]
for e, a in examples:
    print(a, e)
    print(s.minimumCost(**e))
