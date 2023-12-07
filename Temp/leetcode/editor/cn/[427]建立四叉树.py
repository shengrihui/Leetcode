# 427 建立四叉树
from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(x0: int, y0: int, x1: int, y1: int) -> 'Node':
            if x0 == x1:
                return Node(grid[x0][y0], True, None, None, None, None, )
            ok = True
            t = grid[x0][y0]
            for i in range(x0, x1 + 1):
                for j in range(y0, y1 + 1):
                    if grid[i][j] != t:
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                return Node(t, True, None, None, None, None)
            node = Node(t, False, None, None, None, None)
            m = (x1 - x0 + 1) // 2
            node.topLeft = dfs(x0, y0, x1 - m, y1 - m)
            node.topRight = dfs(x0, y0 + m, x1 - m, y1)
            node.bottomLeft = dfs(x0 + m, y0, x1, y1 - m)
            node.bottomRight = dfs(x0 + m, y0 + m, x1, y1)
            return node

        n = len(grid)
        return dfs(0, 0, n - 1, n - 1)
# leetcode submit region end(Prohibit modification and deletion)
