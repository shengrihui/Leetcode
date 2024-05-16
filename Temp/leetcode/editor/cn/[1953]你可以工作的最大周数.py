# 1953 你可以工作的最大周数
# https://leetcode.cn/problems/maximum-number-of-weeks-for-which-you-can-work/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        mx = max(milestones)
        rest = sum(milestones) - mx
        if mx > rest + 1:
            return rest * 2 + 1
        else:
            return rest + mx

# leetcode submit region end(Prohibit modification and deletion)
