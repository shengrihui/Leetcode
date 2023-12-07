# LCP 50 宝石补给
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def giveGem(self, gem: List[int], operations: List[List[int]]) -> int:
        for x, y in operations:
            t = gem[x] // 2
            gem[x] -= t
            gem[y] += t
        return max(gem) - min(gem)

# leetcode submit region end(Prohibit modification and deletion)
