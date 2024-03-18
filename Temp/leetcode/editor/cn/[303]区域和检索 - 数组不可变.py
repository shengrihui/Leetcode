# 303 区域和检索 - 数组不可变
# https://leetcode.cn/problems/range-sum-query-immutable/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class NumArray:

    def __init__(self, nums: List[int]):
        self.pre_sum = list(accumulate(nums, initial=0))

    def sumRange(self, left: int, right: int) -> int:
        return self.pre_sum[right + 1] - self.pre_sum[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# leetcode submit region end(Prohibit modification and deletion)
