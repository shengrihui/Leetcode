# 724 寻找数组的中心下标
# https://leetcode.cn/problems/find-pivot-index/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = s = sum(nums)
        for i, x in enumerate(nums):
            s -= x
            if s == (total - x) / 2:
                return i
        return -1
# leetcode submit region end(Prohibit modification and deletion)
