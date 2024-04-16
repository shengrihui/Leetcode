# 1 两数之和
# https://leetcode.cn/problems/two-sum/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i, x in enumerate(nums):
            if (t := target - x) in d:
                return [d[t], i]
            d[x] = i
# leetcode submit region end(Prohibit modification and deletion)
