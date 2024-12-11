# 2717 半有序排列
# https://leetcode.cn/problems/semi-ordered-permutation/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        a, b = -1, -1
        n = len(nums)
        for i, x in enumerate(nums):
            if x == 1:
                a = i
            if x == n:
                b = i
        return a + n - 1 - b - (b < a)
# leetcode submit region end(Prohibit modification and deletion)
