# 867 转置矩阵
# https://leetcode.cn/problems/transpose-matrix/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return list(zip(*matrix))
# leetcode submit region end(Prohibit modification and deletion)
