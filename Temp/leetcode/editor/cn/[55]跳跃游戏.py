# 55 跳跃游戏
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        most = 0
        n = len(nums)
        for i, x in enumerate(nums):
            if i > most:  # 如果当前的下标是之前的无法达到的，return False
                return False
            most = max(most, i + x)
            if most >= n - 1:
                return True


# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
print(s.canJump([0]))
