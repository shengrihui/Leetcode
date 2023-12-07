# 300 最长递增子序列
import bisect
from typing import *


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i - 1, -1, -1):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        d = []
        for x in nums:
            pos = bisect.bisect_left(d, x)
            if pos >= len(d):
                d.append(x)
            else:
                d[pos] = x
        return len(d)

# leetcode submit region end(Prohibit modification and deletion)
