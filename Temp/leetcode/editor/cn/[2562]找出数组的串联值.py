# 2562 找出数组的串联值
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1
        ans = 0
        while i < j:
            ans += int(str(nums[i]) + str(nums[j]))
            i, j = i + 1, j - 1
        if i == j:
            ans += nums[i]
        return ans
# leetcode submit region end(Prohibit modification and deletion)
