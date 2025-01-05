# 2274 不含特殊楼层的最大连续楼层数
# https://leetcode.cn/problems/maximum-consecutive-floors-without-special-floors/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        return max(y - x - 1 for x, y in pairwise([bottom - 1] + sorted(special) + [top + 1]))
# leetcode submit region end(Prohibit modification and deletion)
