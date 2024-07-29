# 2740 找出分区值
# https://leetcode.cn/problems/find-the-value-of-the-partition/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        return min(y - x for x, y in pairwise(nums))
# leetcode submit region end(Prohibit modification and deletion)
