# 274 H 指数
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        l, r = 0, len(citations) - 1
        while l <= r:
            mid = (l + r) // 2
            if citations[mid] >= mid + 1:
                l = mid + 1
            else:
                r = mid - 1
        return l
# leetcode submit region end(Prohibit modification and deletion)
