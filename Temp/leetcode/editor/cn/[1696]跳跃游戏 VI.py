# 1696 跳跃游戏 VI
# https://leetcode.cn/problems/jump-game-vi/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        @cache
        def dfs(i: int) -> int:
            if i < 0: return 0
            res = -inf
            for j in range(1, k + 1):
                res = max(res, dfs(i - j))
            return res + nums[i]
        return dfs(len(nums) - 1)
# leetcode submit region end(Prohibit modification and deletion)
