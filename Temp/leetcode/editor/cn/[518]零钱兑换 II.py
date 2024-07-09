# 518 零钱兑换 II
# https://leetcode.cn/problems/coin-change-ii/


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for c in coins:
            for t in range(c, amount + 1):
                dp[t] += dp[t - c]
        return dp[amount]
# leetcode submit region end(Prohibit modification and deletion)
