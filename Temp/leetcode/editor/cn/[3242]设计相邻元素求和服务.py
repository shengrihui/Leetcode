# 3242 设计相邻元素求和服务
# https://leetcode.cn/problems/design-neighbor-sum-service/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)

class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.ad = dict()
        self.diag = dict()
        n = len(grid)
        for i in range(n):
            for j in range(n):
                v = grid[i][j]
                a = grid[i - 1][j - 1] if i and j else 0
                b = grid[i - 1][j] if i else 0
                c = grid[i - 1][j + 1] if i and j != n - 1 else 0
                d = grid[i][j - 1] if j else 0
                e = grid[i][j + 1] if j != n - 1 else 0
                f = grid[i + 1][j - 1] if i != n - 1 and j else 0
                g = grid[i + 1][j] if i != n - 1 else 0
                h = grid[i + 1][j + 1] if i != n - 1 and j != n - 1 else 0
                self.ad[v] = b + d + e + g
                self.diag[v] = a + c + f + h

    def adjacentSum(self, value: int) -> int:
        return self.ad[value]

    def diagonalSum(self, value: int) -> int:
        return self.diag[value]

# Your neighborSum object will be instantiated and called as such:
# obj = neighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)

# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)
# leetcode submit region end(Prohibit modification and deletion)
