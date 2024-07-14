# 807 保持城市天际线
# https://leetcode.cn/problems/max-increase-to-keep-city-skyline/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        mx_row = [0] * n
        mx_col = [0] * n
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x > mx_row[i]:
                    mx_row[i] = x
                if x > mx_col[j]:
                    mx_col[j] = x
        ans = 0
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                ans += min(mx_row[i], mx_col[j]) - x
        return ans
# leetcode submit region end(Prohibit modification and deletion)
