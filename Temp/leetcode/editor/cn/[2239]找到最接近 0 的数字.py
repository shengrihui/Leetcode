# 2239 找到最接近 0 的数字
# https://leetcode.cn/problems/find-closest-number-to-zero/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        # res = 100000000
        # for x in nums:
        #     if abs(x) < abs(res):
        #         res = x
        #     elif abs(x) == abs(res):
        #         if x > 0:
        #             res = x
        # return res

        # a 小于 0 的最大值，b 大于 0 的最小值
        a, b = -10000000, 10000000
        for x in nums:
            if x == 0:
                return 0
            if a < x < 0:
                a = x
            elif 0 < x < b:
                b = x
        return a if a + b > 0 else b

# leetcode submit region end(Prohibit modification and deletion)
