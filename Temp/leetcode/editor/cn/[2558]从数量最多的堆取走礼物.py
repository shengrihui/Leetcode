# 2558 从数量最多的堆取走礼物
import heapq
from math import *
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-x for x in gifts]
        heapq.heapify(gifts)
        for _ in range(k):
            x = heapq.heappop(gifts)
            heapq.heappush(gifts, -isqrt(-x))
        return -sum(gifts)
# leetcode submit region end(Prohibit modification and deletion)
