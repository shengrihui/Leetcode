# 2530 执行 K 次操作后的最大分数
import heapq
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-x for x in nums]
        q = heapq.heapify(nums)
        ans = 0
        for _ in range(k):
            x = heapq.heappop(nums)
            ans += -x
            # heapq.heappush(nums, -((-x) // 3 + 1))  # 3的倍数算不对
            # heapq.heappush(nums, -((-x) // 3 + ((-x) % 3 != 0)))  # 3的倍数算不对
            heapq.heappush(nums, -((-x + 2) // 3))  # 3的倍数算不对
        return ans
# leetcode submit region end(Prohibit modification and deletion)
