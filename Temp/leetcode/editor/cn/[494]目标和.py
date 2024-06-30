# 494 目标和
# https://leetcode.cn/problems/target-sum/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def dfs(i: int, c: int) -> int:
            if i == -1:
                return c == target
            return dfs(i - 1, c + nums[i]) + dfs(i - 1, c - nums[i])

        return dfs(len(nums) - 1, 0)

# leetcode submit region end(Prohibit modification and deletion)
