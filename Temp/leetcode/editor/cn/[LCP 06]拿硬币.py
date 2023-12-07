# LCP 06 拿硬币
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minCount(self, coins: List[int]) -> int:
        return sum((i + 1) // 2 for i in coins)
# leetcode submit region end(Prohibit modification and deletion)
