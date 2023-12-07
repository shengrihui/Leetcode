# 122 买卖股票的最佳时机 II
from itertools import *
from typing import *


# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         ans = 0
#         mn = mx = prices[0]
#         for x in prices:
#             if x > mx:
#                 mx = x
#                 ans += mx - mn
#             mn = mx = x
#         return ans
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(y - x for x, y in pairwise(prices) if y > x)

# leetcode submit region end(Prohibit modification and deletion)
