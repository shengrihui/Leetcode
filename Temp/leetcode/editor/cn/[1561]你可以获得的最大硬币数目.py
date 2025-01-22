# 1561 你可以获得的最大硬币数目
# https://leetcode.cn/problems/maximum-number-of-coins-you-can-get/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        return sum(piles[len(piles) // 3::2])
# leetcode submit region end(Prohibit modification and deletion)
