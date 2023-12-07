# 2731 移动机器人
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        MOD = 10 ** 9 + 7
        for i in range(len(nums)):
            nums[i] += d if s[i] == "R" else -d
        nums.sort()
        ans = s = 0  # s前缀和
        # (a[i] - a[0]) + (a[i] - a[1]) + ... + (a[i] - a[i - 1])
        # =a[i] * i - s
        for i, x in enumerate(nums):
            ans = (ans + x * i + s) % MOD
            s += x
        return ans

# leetcode submit region end(Prohibit modification and deletion)
