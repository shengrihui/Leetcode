# 213 打家劫舍 II
from typing import *


class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob2(start, end):
            # start和end是nums下标,[start,end],nums[start:end+1]
            m = end - start + 1
            dp = [0] * m
            dp[0] = nums[start]
            dp[1] = max(nums[start], nums[start + 1])
            for i in range(2, m):
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[start + i])
            return dp[-1]

        n = len(nums)
        if n <= 2:
            return max(nums)
        return max(rob2(0, n - 2), rob2(1, n - 1))


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob3(start, end):
            f0, f1 = 0, 0
            for i in range(start, end + 1):
                f0, f1 = f1, max(f1, nums[i] + f0)

            return f1

        n = len(nums)
        return max(nums[0], rob3(0, n - 2), rob3(1, n - 1))


# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
print(s.rob([2]))
