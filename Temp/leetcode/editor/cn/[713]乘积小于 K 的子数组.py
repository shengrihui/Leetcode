# 713 乘积小于 K 的子数组
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:  # k=1没法 严格小于
            return 0
        left = 0
        ans = 0
        prod = 1
        for right, x in enumerate(nums):
            prod *= x
            # 如果没有前面 k<=1 的特判，要 left <= right
            # while left <= right and prod >= k:
            # 有特判更快一些
            while prod >= k:
                prod /= nums[left]
                left += 1
            ans += right - left + 1
        return ans
# leetcode submit region end(Prohibit modification and deletion)
