# 287 寻找重复数
from collections import *
from typing import *


# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         n = len(nums) - 1
#         arr = [n, 1, n + 1, 0]
#         return reduce(lambda x, y: x ^ y, nums, arr[n % 4])

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for k, v in Counter(nums).items():
            if v > 1:
                return k
# leetcode submit region end(Prohibit modification and deletion)
