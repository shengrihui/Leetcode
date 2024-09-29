# 2073 买票需要的时间
# https://leetcode.cn/problems/time-needed-to-buy-tickets/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        return sum(min(t, tickets[k] - (i > k)) for i, t in enumerate(tickets))
# leetcode submit region end(Prohibit modification and deletion)
