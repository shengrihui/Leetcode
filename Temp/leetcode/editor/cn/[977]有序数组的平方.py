# 977 有序数组的平方
# https://leetcode.cn/problems/squares-of-a-sorted-array/

from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # return sorted([x ** 2 for x in nums])
        n = len(nums)
        i, j = 0, n - 1
        ans = [0] * n
        for p in range(n - 1, -1, -1):
            x, y = nums[i], nums[j]
            if -x > y:
                ans[p] = x * x
                i += 1
            else:
                ans[p] = y * y
                j -= 1
        return ans
# leetcode submit region end(Prohibit modification and deletion)
