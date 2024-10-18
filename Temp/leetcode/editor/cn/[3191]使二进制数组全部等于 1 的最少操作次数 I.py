# 3191 使二进制数组全部等于 1 的最少操作次数 I
# https://leetcode.cn/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums) - 2):
            if nums[i] == 0:
                nums[i + 1] ^= 1
                nums[i + 2] ^= 1
                ans += 1
        return ans if nums[-1] and nums[-2] else -1
# leetcode submit region end(Prohibit modification and deletion)
