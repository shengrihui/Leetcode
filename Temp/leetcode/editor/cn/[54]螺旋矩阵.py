# 54 螺旋矩阵
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row, col = len(matrix), len(matrix[0])
        n = row * col
        ans = []
        i = j = 0
        DIR = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d = 0
        si = sj = 0
        ei, ej = row - 1, col - 1
        while si <= i <= ei and sj <= j <= ej:
            ans.append(matrix[i][j])
            if d == 0 and j == ej:
                si += 1
                d = 1
            elif d == 1 and i == ei:
                ej -= 1
                d = 2
            elif d == 2 and j == sj:
                ei -= 1
                d = 3
            elif d == 3 and i == si:
                sj += 1
                d = 0
            di, dj = DIR[d]
            i, j = i + di, j + dj
        return ans

# leetcode submit region end(Prohibit modification and deletion)

# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
#  
# 
#  示例 2： 
#  
#  
# 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == matrix.length 
#  n == matrix[i].length 
#  1 <= m, n <= 10 
#  -100 <= matrix[i][j] <= 100 
#  
# 
#  Related Topics 数组 矩阵 模拟 👍 1513 👎 0
