# 1962 移除石子使总数最小
# https://leetcode.cn/problems/remove-stones-to-minimize-the-total/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        q = [-p for p in piles]
        heapq.heapify(q)
        for _ in range(k):
            x = heapq.heappop(q)
            heapq.heappush(q, x // 2)
        return -sum(q)
# leetcode submit region end(Prohibit modification and deletion)
