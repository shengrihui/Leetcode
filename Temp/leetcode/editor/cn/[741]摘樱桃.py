# 741 摘樱桃
# https://leetcode.cn/problems/cherry-pickup/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # dp[k][i1][i2] 第 k 步第 1 个点在第 i1(1-index) 行，第 2 个点在第 i2 行樱桃的最大值
        # k = i1 + j1
        # 第一个人的坐标 (i1,k-i1) 一开始第 2 步，最后第 2n 步
        # 初始 dp[2][1][1] = grid[0][0] 第 2 步两个点都在 (1,1)
        dp = [[[-inf] * (n + 1) for _ in range(n + 1)] for _ in range(2 * n + 1)]
        dp[2][1][1] = grid[0][0]
        for k in range(3, 2 * n + 1):
            for i1 in range(1, n + 1):
                j1 = k - i1
                if not 1 <= j1 <= n or (A := grid[i1 - 1][j1 - 1]) == -1:
                    continue
                for i2 in range(1, n + 1):
                    j2 = k - i2
                    if j2 <= 0 or j2 > n or (B := grid[i2 - 1][j2 - 1]) == -1:
                        continue
                    # 两个点的来源
                    a, b, c, d = dp[k - 1][i1 - 1][i2], dp[k - 1][i1][i2 - 1], \
                        dp[k - 1][i1 - 1][i2 - 1], dp[k - 1][i1][i2]
                    t = max(a, b, c, d) + A
                    if i1 != i2:
                        t += B
                    dp[k][i1][i2] = t
        return dp[-1][-1][-1] if dp[-1][-1][-1] > 0 else 0
    # leetcode submit region end(Prohibit modification and deletion)
