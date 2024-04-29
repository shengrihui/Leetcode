# 1329 将矩阵按对角线排序
# https://leetcode.cn/problems/sort-the-matrix-diagonally/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        # mat[i][j]  i = j + k
        # k: [-(n-1),m-1]                range(1-n,m)
        # i: [max(0,k), min(m-1,n-1+k)]  range(max(0,k), min(m,n+k))
        for k in range(1 - n, m):
            i_range = range(max(0, k), min(m, n + k))
            a = sorted(mat[i][i - k] for i in i_range)
            for i, v in zip(i_range, a):
                mat[i][i - k] = v
        return mat

# leetcode submit region end(Prohibit modification and deletion)
