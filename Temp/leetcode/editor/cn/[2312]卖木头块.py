# 2312 卖木头块
# https://leetcode.cn/problems/selling-pieces-of-wood/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        @cache
        def dfs(height: int, width: int) -> int:
            # if height <= 0 or width <= 0:
            #     return 0
            res = 0
            for h, w, p in prices:
                if h < height and w < width:
                    res = max(res, p + dfs(height - h, width) + dfs(h, width),
                              p + dfs(height, width - w) + dfs(height, w))
            return res

        return dfs(m, n)

        # dp = [[0] * (n + 1) for _ in range(m + 1)]
        # for h, v, p in prices:
        #     dp[h][v] = p
        # prices.sort()
        # for i in range(1, m + 1):
        #     for j in range(1, n + 1):
        #         for h, v, p in prices:
        #             if h > i: break
        #             if v > j: continue
        #             dp[i][j] = max(dp[i][j],  dp[i - h][j] + dp[h][j],  dp[i][v] + dp[i][j - v])
        #
        # return dp[-1][-1]
# leetcode submit region end(Prohibit modification and deletion)
