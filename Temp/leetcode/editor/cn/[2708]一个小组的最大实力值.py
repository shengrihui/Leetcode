# 2708 一个小组的最大实力值
# https://leetcode.cn/problems/maximum-strength-of-a-group/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        mn = mx = nums[0]
        for x in nums[1:]:
            mn, mx = min(x, mn, mn * x, mx * x), max(x, mx, mn * x, mx * x)
        return mx
# leetcode submit region end(Prohibit modification and deletion)
