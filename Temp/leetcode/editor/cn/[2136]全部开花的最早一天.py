# 2136 全部开花的最早一天
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        ans = 0
        p = 0
        for gt, pt in sorted(zip(growTime, plantTime), key=lambda x: -x[0]):
            ans = max(ans, p + pt + gt)
            p += pt
        return ans
# leetcode submit region end(Prohibit modification and deletion)
