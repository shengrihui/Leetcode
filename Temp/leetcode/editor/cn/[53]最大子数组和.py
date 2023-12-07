# 53 最大子数组和
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
# dp[i]： nums到 i 结尾的最大子数组和
# 因为nums[i]有负数，所以dp[i - 1] + nums[i]可能会更小
# 考虑的两种情况是nums[i]是否加入dp[i-1]，加入还是另起一段
# 要让和尽量大，非负数肯定要尽可能多，
# 如果 dp[i - 1] + nums[i] 比 nums[i]要小了，说明这段子数组也就到此为止了，
# 再往后如果加到前面去也不会是更好的答案了
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # n = len(nums)
        # dp = [0] * n
        # dp[0] = nums[0]
        # for i in range(1, n):
        #     dp[i] = max(dp[i - 1] + nums[i], nums[i])
        # return max(dp)
        ans = nums[0]
        pre = 0
        for x in nums:
            pre = max(pre + x, x)
            ans = max(pre, ans)
        return ans

# leetcode submit region end(Prohibit modification and deletion)
