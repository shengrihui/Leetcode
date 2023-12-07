# 152 乘积最大子数组
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        min_dp = [0] * n
        max_dp = [0] * n
        min_dp[0] = max_dp[0] = nums[0]
        for i in range(1, n):
            #  * (min_dp[i - 1] if nums[i] > 0 else max_dp[i - 1])
            # 如果 nums[i]是正数，nums[i]要乘较小的数（负数）才能更小
            # 好要与nums[i]取min避免0的情况
            min_dp[i] = min(nums[i], nums[i] * (min_dp[i - 1] if nums[i] > 0 else max_dp[i - 1]))
            max_dp[i] = max(nums[i], nums[i] * (max_dp[i - 1] if nums[i] > 0 else min_dp[i - 1]))
        return max(max_dp)

# leetcode submit region end(Prohibit modification and deletion)
