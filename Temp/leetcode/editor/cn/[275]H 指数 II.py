# 275 H 指数 II
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if citations[mid] >= n - mid:
                r = mid - 1
            else:
                l = mid + 1
        return n - l
# leetcode submit region end(Prohibit modification and deletion)
