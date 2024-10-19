# 908 最小差值 I
# https://leetcode.cn/problems/smallest-range-i/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        mn, mx = min(nums), max(nums)
        return 0 if mx - mn <= 2 * k else mx - mn - 2 * k

# leetcode submit region end(Prohibit modification and deletion)
