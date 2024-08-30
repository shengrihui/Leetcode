# 3127 构造相同颜色的正方形
# https://leetcode.cn/problems/make-a-square-with-the-same-color/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        for i, row in enumerate(grid):
            for j, c in enumerate(row):
                if i and grid[i - 1][j] == c or i < 2 and c == grid[i + 1][j]:
                    if j < 2 and c == grid[i][j + 1] or j and c == grid[i][j - 1]:
                        return True
        return False


"""
class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        for i in range(2):
            for j in range(2):
                cnt = 0
                for p in range(2):
                    for q in range(2):
                        if grid[i+p][q+j]=='B':
                            cnt += 1
                if cnt!=2:
                    return True
        return False
"""
# leetcode submit region end(Prohibit modification and deletion)
