# 688 骑士在棋盘上的概率
# https://leetcode.cn/problems/knight-probability-in-chessboard/
from imports import *

# leetcode submit region begin(Prohibit modification and deletion)
# https://leetcode.cn/problems/knight-probability-in-chessboard/solutions/2997395/jiao-ni-yi-bu-bu-si-kao-dpcong-ji-yi-hua-dgt6
DIRS = (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)


class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        @cache
        def dfs(k: int, r: int, c: int) -> float:
            if not (0 <= r < n and 0 <= c < n):
                return 0
            if k == 0:
                return 1
            return sum(dfs(k - 1, r - dr, c - dc) for dr, dc in DIRS) / 8

        return dfs(k, row, column)
# leetcode submit region end(Prohibit modification and deletion)
