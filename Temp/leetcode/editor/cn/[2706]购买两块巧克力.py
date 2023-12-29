# 2706 购买两块巧克力
# https://leetcode.cn/problems/buy-two-chocolates/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        rest = money - prices[0] - prices[1]
        return rest if rest >= 0 else money
# leetcode submit region end(Prohibit modification and deletion)
