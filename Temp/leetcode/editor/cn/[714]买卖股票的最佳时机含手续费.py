# 714 买卖股票的最佳时机含手续费
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        buy, sell = [0] * n, [0] * n
        sell = [0] * n
        buy[0] = -prices[0]
        for i in range(1, n):
            buy[i] = max(buy[i - 1], sell[i - 1] - prices[i])  # max(之前买入今天不卖出（今天依然持有），之前卖出今天新买入)
            sell[i] = max(sell[i - 1], buy[i - 1] + prices[i] - fee)  # max(今天不买，今天卖出手头持有的)
        return sell[-1]

# leetcode submit region end(Prohibit modification and deletion)
