# 121 买卖股票的最佳时机
from typing import *


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        right_max = [0] * n
        right_max[-1] = prices[-1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], prices[i])
        ans = 0
        for i, x in enumerate(prices):
            ans = max(right_max[i] - x, ans)
        return max(ans, 0)


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        r_max = prices[-1]
        ans = 0
        for i in range(n - 2, -1, -1):
            ans = max(ans, r_max - prices[i])
            r_max = max(r_max, prices[i])
        return ans
# leetcode submit region end(Prohibit modification and deletion)
