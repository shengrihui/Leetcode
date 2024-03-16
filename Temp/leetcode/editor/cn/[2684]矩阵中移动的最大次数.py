# 2684 矩阵中移动的最大次数
# https://leetcode.cn/problems/maximum-number-of-moves-in-a-grid/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
# class Solution:
#     def maxMoves(self, grid: List[List[int]]) -> int:
#         m, n = len(grid), len(grid[0])
#         dp = [[0] * n for _ in range(m)]
#         for col in range(n - 2, -1, -1):
#             for row in range(m):
#                 for i in range(-1, 2):
#                     if 0 <= row + i < m:
#                         if grid[row + i][col + 1] > grid[row][col]:
#                             dp[row][col] = max(dp[row][col], dp[row + i][col + 1] + 1)
#         return max(dp[i][0] for i in range(m))

class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque(range(m))
        for col in range(n - 1):
            vis = set()
            for _ in range(len(q)):
                row = q.popleft()
                for i in range(-1, 2):
                    nr = row + i
                    if 0 <= nr < m and nr not in vis and grid[nr][col + 1] > grid[row][col]:
                        q.append(nr)
                        vis.add(nr)
            if not q:
                return col
        return n - 1

# leetcode submit region end(Prohibit modification and deletion)
