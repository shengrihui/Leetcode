# 2008 出租车的最大盈利
# https://leetcode.cn/problems/maximum-earnings-from-taxi/
from imports import *

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        groups = [[] for _ in range(n + 1)]
        for start, end, tip in rides:
            groups[end].append([start, end - start + tip])

        # 记忆化搜索
        """
        # dfs(i) 返回到 i 的最大盈利
        # 两个转移来源：
        # 1. i 有乘客，遍历 end=i 的乘客，dfs(start)+ price
        # 2. i 没有乘客，就是 dfs(i-1)
        @cache
        def dfs(i: int) -> int:
            if i == 1:
                return 0
            res = dfs(i - 1)
            for start, price in groups[i]:
                res = max(res, dfs(start) + price)
            return res
        return dfs(n)
        """
        dp = [0 for _ in range(n + 1)]
        for end in range(1, n + 1):
            dp[end] = dp[end - 1]
            for start, price in groups[end]:
                dp[end] = max(dp[start] + price, dp[end])
        return dp[-1]

# leetcode submit region end(Prohibit modification and deletion)
