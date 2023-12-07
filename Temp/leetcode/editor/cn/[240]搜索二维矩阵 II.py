# 240 搜索二维矩阵 II
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        x, y = 0, col - 1
        while x < row and y >= 0:
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] > target:
                y -= 1
            else:
                x += 1
        return False
# leetcode submit region end(Prohibit modification and deletion)
