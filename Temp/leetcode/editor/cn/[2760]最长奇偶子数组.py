# 2760 最长奇偶子数组
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        ans = 0
        l = 0
        flag = False
        for i, x in enumerate(nums):
            if flag and (x > threshold or x % 2 == nums[i - 1] % 2):
                ans = max(ans, i - l)
                flag = False
            if not flag and x % 2 == 0 and x <= threshold:
                l = i
                flag = True
        return max(ans, len(nums) - l if flag else 0)
# leetcode submit region end(Prohibit modification and deletion)
