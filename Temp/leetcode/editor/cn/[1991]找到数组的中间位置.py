# 1991 找到数组的中间位置
# https://leetcode.cn/problems/find-the-middle-index-in-array/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total = s = sum(nums)
        for i, x in enumerate(nums):
            s -= x
            if s == (total - x) / 2:
                return i
        return -1
# leetcode submit region end(Prohibit modification and deletion)
