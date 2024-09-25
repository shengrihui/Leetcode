# 2535 数组元素和与数字和的绝对差
# https://leetcode.cn/problems/difference-between-element-sum-and-digit-sum-of-an-array/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        a = b = 0
        for x in nums:
            a += x
            while x:
                b += x % 10
                x //= 10
        return abs(a - b)
# leetcode submit region end(Prohibit modification and deletion)
