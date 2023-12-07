# 209 长度最小的子数组
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        n = len(nums)
        ans = n + 1
        s = 0
        for right, x in enumerate(nums):
            s += x
            # while s >= target:
            #     ans = min(ans, right - left + 1)
            #     s -= nums[left]
            #     left += 1
            #######################################
            while s - nums[left] >= target:
                s -= nums[left]
                left += 1
            # 退出 while 后，[下一个left,right] 的和就不  >= target
            if s >= target:  # 刚开始的时候，s 会小于 target
                ans = min(ans, right - left + 1)
        return ans if ans != n + 1 else 0

# leetcode submit region end(Prohibit modification and deletion)
