# 3192 使二进制数组全部等于 1 的最少操作次数 II
# https://leetcode.cn/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-ii/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        for x in nums:
            if x == ans % 2:
                ans += 1
        return ans
# leetcode submit region end(Prohibit modification and deletion)
