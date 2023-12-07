# 62 不同路径
import math


# leetcode submit region begin(Prohibit modification and deletion)
# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         dp = [[0] * n for _ in range(m)]
#         for i in range(m):
#             dp[i][0] = 1
#         for j in range(n):
#             dp[0][j] = 1
#         for i in range(1, m):
#             for j in range(1, n):
#                 dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
#         return dp[-1][-1]

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 一共要走 m+n-2 步，其中 m-1 个向下
        return math.comb(m + n - 2, m - 1)
# leetcode submit region end(Prohibit modification and deletion)
