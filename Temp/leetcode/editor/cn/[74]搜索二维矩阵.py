# 74 搜索二维矩阵
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        l, r = 0, n * m - 1
        while l <= r:
            mid = (l + r) // 2
            row, col = mid // m, mid % m
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False
# leetcode submit region end(Prohibit modification and deletion)
