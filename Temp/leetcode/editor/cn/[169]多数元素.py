# 169 多数元素
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         return [k for k, v in Counter(nums).items() if v > len(nums) // 2][0]

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = candidate = 0
        for x in nums:
            if count == 0:
                candidate = x
            count += 1 if candidate == x else -1
        return candidate
# leetcode submit region end(Prohibit modification and deletion)
