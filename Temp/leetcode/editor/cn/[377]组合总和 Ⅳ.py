# 377 组合总和 Ⅳ
# https://leetcode.cn/problems/combination-sum-iv/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target + 1):
            for x in nums:
                if x <= i:
                    dp[i] += dp[i - x]
        return dp[target]

# leetcode submit region end(Prohibit modification and deletion)
