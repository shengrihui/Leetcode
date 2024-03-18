# 2642 设计可以求最短路径的图类
# https://leetcode.cn/problems/design-graph-with-shortest-path-calculator/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.g = [[inf] * n for _ in range(n)]
        for x, y, c in edges:
            self.g[x][y] = c
        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    if i == j:
                        self.g[i][j] = 0
                        continue
                    self.g[i][j] = min(self.g[i][j], self.g[i][k] + self.g[k][j])

    def addEdge(self, edge: List[int]) -> None:
        x, y, c = edge
        self.g[x][y] = min(self.g[x][y], c)
        for k in [x, y]:
            for i in range(self.n):
                for j in range(self.n):
                    if i == j: continue
                    self.g[i][j] = min(self.g[i][j], self.g[i][k] + self.g[k][j])

    def shortestPath(self, node1: int, node2: int) -> int:

        return self.g[node1][node2] if self.g[node1][node2] != inf else -1

# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
# leetcode submit region end(Prohibit modification and deletion)
