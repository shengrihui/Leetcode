# 416 分割等和子集
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2:  # 如果nums的总和是奇数，肯定分成不了两部分
            return False
        n = len(nums)
        dp = [False] * (s // 2 + 1)
        dp[0] = True
        for x in nums:
            for i in range(s // 2, x - 1, -1):  # 必须从后往前
                dp[i] |= dp[i - x]  # 将x加到能组成i-x上，dp[i]=True
        return dp[-1]
# leetcode submit region end(Prohibit modification and deletion)
