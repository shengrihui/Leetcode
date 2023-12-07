# 123 买卖股票的最佳时机 III
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        left = [0] * n
        mn = prices[0]
        right = [0] * n
        mx = prices[-1]
        for i in range(1, n):
            mn = min(mn, prices[i])
            left[i] = max(left[i - 1], prices[i] - mn)
            ii = n - 1 - i
            mx = max(mx, prices[ii])
            right[ii] = max(right[ii + 1], mx - prices[ii])
        ans = right[0]
        for i in range(n - 1):
            ans = max(ans, left[i] + right[i + 1])
        return ans
# leetcode submit region end(Prohibit modification and deletion)
