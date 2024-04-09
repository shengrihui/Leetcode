# 2529 正整数和负整数的最大计数
# https://leetcode.cn/problems/maximum-count-of-positive-integer-and-negative-integer/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        a = bisect_left(nums, 0)
        b = bisect_left(nums, 1)
        return max(a, len(nums) - b)
# class Solution:
#     def maximumCount(self, nums: List[int]) -> int:
#         pos = neg = 0
#         for x in nums:
#             if x > 0:
#                 pos += 1
#             elif x < 0:
#                 neg += 1
#         return pos if pos > neg else neg
# leetcode submit region end(Prohibit modification and deletion)
